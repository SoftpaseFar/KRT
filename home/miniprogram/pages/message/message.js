// pages/message/message.js
Page({

  /**
   * Page initial data
   */
  data: {
    message_category: ['个人消息', '系统消息'],
    roomId: "",
    scategory_elect_idx: 0,


    message_list: [{
        "roomid": 0,
        "date": "2022-1-1 20:00",
        "is_read": false,
        "name": "接送孩子",
        "last_message": "你好"
      }, {
        "roomid": 1,
        "date": "2022-1-1 20:00",
        "is_read": true,
        "name": "婚庆",
        "last_message": "好的"
      }, {
        "roomid": 2,
        "date": "2022-1-1 20:00",
        "is_read": false,
        "name": "拿快递",
        "last_message": "表情"
      },
      {
        "roomid": 3,
        "date": "2022-1-1 20:00",
        "is_read": false,
        "name": "接送孩子",
        "last_message": "你好"
      }, {
        "roomid": 4,
        "date": "2022-1-1 20:00",
        "is_read": true,
        "name": "婚庆",
        "last_message": "好的"
      }, {
        "roomid": 5,
        "date": "2022-1-1 20:00",
        "is_read": false,
        "name": "拿快递",
        "last_message": "表情"
      },
      {
        "roomid": 6,
        "date": "2022-1-1 20:00",
        "is_read": false,
        "name": "接送孩子",
        "last_message": "你好"
      }, {
        "roomid": 7,
        "date": "2022-1-1 20:00",
        "is_read": true,
        "name": "婚庆",
        "last_message": "好的"
      }, {
        "roomid": 8,
        "date": "2022-1-1 20:00",
        "is_read": false,
        "name": "拿快递",
        "last_message": "表情"
      },
      {
        "roomid": 9,
        "date": "2022-1-1 20:00",
        "is_read": false,
        "name": "接送孩子",
        "last_message": "你好"
      }, {
        "roomid": 10,
        "date": "2022-1-1 20:00",
        "is_read": true,
        "name": "婚庆",
        "last_message": "好的"
      }, {
        "roomid": 11,
        "date": "2022-1-1 20:00",
        "is_read": false,
        "name": "拿快递",
        "last_message": "表情"
      }
    ]

  },

  select_category: function (e) {
    let idx = e.currentTarget.dataset.index;
    console.log(idx);
    this.setData({
      scategory_elect_idx:idx
    });
  },
  select_one_list: function (e) {
    let idx = e.currentTarget.dataset.index;
    console.log(idx);
    this.setData({
      roomId: idx
    });
    wx.navigateTo({
      url: '/pages/index/index?roomId=' + this.data.roomId+'&title='+this.data.message_list[idx]['name'],
      fail(e) {
        console.log(e)
      }
    })
  },

  /**
   * Lifecycle function--Called when page load
   */
  onLoad(options) {

  },

  /**
   * Lifecycle function--Called when page is initially rendered
   */
  onReady() {

  },

  /**
   * Lifecycle function--Called when page show
   */
  onShow() {

  },

  /**
   * Lifecycle function--Called when page hide
   */
  onHide() {

  },

  /**
   * Lifecycle function--Called when page unload
   */
  onUnload() {

  },

  /**
   * Page event handler function--Called when user drop down
   */
  onPullDownRefresh() {

  },

  /**
   * Called when page reach bottom
   */
  onReachBottom() {

  },

  /**
   * Called when user click on the top right corner to share
   */
  onShareAppMessage() {

  },



})
