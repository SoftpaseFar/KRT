const cloud = require('wx-server-sdk')
cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV
})
const db = cloud.database();
const _ = db.command;
const BUSER = 'cloud-users-ban';
// 时间工具类
const timeutil = require('./timeutil');
// 云函数入口函数
exports.main = async (event, context) => {
  const wxContext = cloud.getWXContext()
  // 待封禁的用户openid
  let openid = event.openid 
  // 封禁时长 单位 天
  let ban_date = 30
  try {
    //获取用户封禁信息 更新封禁信息
    let userBan = await db.collection(BUSER).doc(openid).get();
    let userBanData = userBan.data;
    return await db.collection(BUSER).doc(openid).update({
      data:{
        _updateTime:timeutil.TimeCode(),
        ban_date:_.inc(ban_date)
      }
    })
  } catch (error) {
    // 不存在该用户封禁信息 新建并写入
    return await db.collection(BUSER).doc(openid).set({
      data:{
        ban_date,
        openid,
        _createTime:timeutil.TimeCode(),
        _updateTime:timeutil.TimeCode()
      }
    })
  }
 
}