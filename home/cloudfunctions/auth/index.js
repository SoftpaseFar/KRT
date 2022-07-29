// 云函数入口文件
const cloud = require('wx-server-sdk')
cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV
})
const db = cloud.database();
const _ = db.command;
// 用户
const USERS = 'chat-users';
// 云函数入口函数
exports.main = async (event, context) => {
  const wxContext = cloud.getWXContext()
  let openid = wxContext.OPENID;
  try {
    let res =  await db.collection(USERS).doc(openid).get();
    return {
      errMsg:'cloud.callFunction:ok',
      result:res.data
    }
  } catch (error) {
    return {
      errMsg:'cloud.auth:false',
      errCode:-1
    }
  }
}