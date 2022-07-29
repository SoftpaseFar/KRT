const cloud = require('wx-server-sdk')
const crypto = require('crypto');
cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV
})
const db = cloud.database();
const _ = db.command;
// 时间工具类
const timeutil = require('./timeutil');

// 用户信息表名称
const USER = 'chat-users';
// 用户信息记录表
const MSG = 'chat-msgs';
// 用户违法消息记录表
const MSG_BAN = 'chat-msgs-ban';
// 用户禁言名单
const BUSER = 'chat-users-ban';
// 云函数入口函数 
exports.main = async (event, context) => {
  const wxContext = cloud.getWXContext()
  // 获取用户唯一身份识别ID
  let openid = wxContext.OPENID || event.openid;
  let _userInfo_ = await db.collection(USER).doc(openid).get();
  // 获取用户信息
  let userInfo = _userInfo_.data.userInfo;
  // 获取消息类型
  let msgType = event.msgType || 'text';
  // 获取会话房间号
  let roomId = event.roomId || 1
  // 根据用户openid 查询用户是否在黑名单内
  let banData = null;
  try {
    banData = await db.collection(BUSER).doc(openid).get();
    let userBan = banData.data;
    if(userBan.ban_date > 0){
      // 用户禁言时间大于 0 
      return {
        code:300,
        msg:'禁言时长还剩'+userBan.ban_date+'天'
      }
    }
  } catch (error) {
    console.log('--无禁言记录--')
  }
  // 根据消息类型 -- 进行不同逻辑处理
  switch (msgType) {
    case 'text': {
      // 获取消息主体内容
      let content = event.content;
      // 安全内容审查
      let res = await ContentSafe(content)
      console.log(res)
      if (res.result.code == 200) {
        // 内容安全校验通过写入数据
        return await db.collection(MSG).add({
          data: {
            roomId,
            openid,
            msgType,
            content,
            userInfo,
            _createTime: timeutil.TimeCode()
          }
        })
      } else {
        //发布违规内容的写入记录表
        await db.collection(MSG_BAN).add({
          data: {
            roomId,
            openid,
            msgType,
            content,
            userInfo,
            _createTime: timeutil.TimeCode()
          }
        })
        return res.result
      }
      break
    }
    case 'image': {
      let content = event.content;
      let res = await ImageSafe(event.content)
      console.log(res)
      //将图片传入云存储
      const hash = crypto.createHash('md5');
      hash.update(content, 'utf8');
      const md5 = hash.digest('hex');
      console.log('--文件唯一MD5编码--')
      console.log(md5);
      let upData = await cloud.uploadFile({
        cloudPath: 'cloud-chat/'+md5+'.png',
        fileContent: Buffer.from(content,'base64')
      })
      console.log(upData)
      let fileID = upData.fileID;
      if (res.result.code == 200) {
        // 内容安全校验通过写入数据
        return await db.collection(MSG).add({
          data: {
            roomId,
            openid,
            msgType,
            content:fileID,
            userInfo,
            _createTime: timeutil.TimeCode()
          }
        })
      } else {
        //发布违规内容的写入记录表
        await db.collection(MSG_BAN).add({
          data: {
            roomId,
            openid,
            msgType,
            content:fileID,
            userInfo,
            _createTime: timeutil.TimeCode()
          }
        })
        return res.result
      }
      break
    }
  }
}
async function ContentSafe(content) {
  //文本内容安全校验
  return await cloud.callFunction({
    name: 'openapi',
    data: {
      action: 'msgSecCheck',
      content: content
    }
  })
}
async function ImageSafe(content) {
  // console.log(content)
  //图片内容安全校验
  return await cloud.callFunction({
    name: 'openapi',
    data: {
      action: 'imgSecCheck',
      contentType: 'image/png',
      value: content
    }
  })
}