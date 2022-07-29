const cloud = require('wx-server-sdk')
cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV
})
const db = cloud.database();
const _ = db.command;
const BUSER = 'chat-users-ban';

// 云函数入口函数
exports.main = async (event, context) => {
  return await db.collection(BUSER).where({
    ban_date:_.gt(0)
  }).update({
    data:{
      ban_date:_.inc(-1)
    }
  })
}