const cloud = require('wx-server-sdk')
cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV
})
const db = cloud.database();
const _ = db.command;
// 消息记录表
const MSG = 'chat-msgs';
// 云函数入口函数
exports.main = async (event, context) => {
  const wxContext = cloud.getWXContext()
  // 用户身份唯一识别ID
  var openid = wxContext.OPENID;
  // 获取步骤
  let step = event.step;
  // 获取房间号
  let roomId = event.roomId || 1;
  return await db.collection(MSG).where({
    roomId
  }).skip(step).limit(20).orderBy('_createTime','desc').get();
}