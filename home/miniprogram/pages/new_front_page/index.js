Page({

  /**
   * 页面的初始数据
   */
  data: {
    // 顶部动画
    top_help: true,
    top_publish: true,

    // 轮播
    currentIndex: 0,
    background: ['https://tse2-mm.cn.bing.net/th/id/OIP-C.0-8KaD4ntl-KaJrrb-S_KQHaGO?pid=ImgDet&rs=1', 'https://img.zcool.cn/community/01b6bb579393330000018c1b442807.jpg@1280w_1l_2o_100sh.jpg', 'https://img.zcool.cn/community/013d33579393330000012e7ec25322.jpg@1280w_1l_2o_100sh.jpg'],

    //顶部定位与搜索
    // top_loc_and_pub_style: "",
    // search_style: "width: 56%;",


  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady() {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage() {

  },

  // 拨打110
  call_110() {
    wx.vibrateShort(); // 1、使手机震动15ms
    wx.makePhoneCall({
      phoneNumber: '110',
    })
  },
  help_effect_open(e) {
    var name = e.currentTarget.dataset.name;
    // console.log(name);
    this.animate(
      name,
      [{
          width: "7%",
          backgroundColor: "rgba(138, 44, 226,0.6)",
        },
        {
          width: "50%",
          backgroundColor: "rgba(138, 44, 226,1)",
        },
      ],
      200,
      function () {
        // console.log("111");
      }.bind(this)
    );
    if (name == '.top_options_help') {
      this.setData({
        top_help: !this.data.top_help
      });
    } else {
      this.setData({
        top_publish: !this.data.top_publish
      });
    }
  },

  // 论坛
  call_forum() {
    console.log("进入论坛");
  },

  search() {
    console.log("11");
    wx.navigateTo({
      url: '/pages/historySearch/index',
      fail(e) {
        console.log(e)
      }
    })
  },

  help_effect_close(e) {
    var name = e.currentTarget.dataset.name;
    this.animate(
      name,
      [{
          width: "50%",
          backgroundColor: "rgba(138, 44, 226,1)",
        },
        {
          width: "7%",
          backgroundColor: "rgba(138, 44, 226,0.6)",
        },
      ],
      200,
      function () {
        // console.log("111");
      }.bind(this)
    );
    if (name == '.top_options_help') {
      // console.log("1");
      this.setData({
        top_help: !this.data.top_help
      });
    } else {
      // console.log("2");
      this.setData({
        top_publish: !this.data.top_publish
      });
    }
  },

  // 轮播
  /* 这里实现控制中间凸显图片的样式 */
  handleChange: function (e) {
    this.setData({
      currentIndex: e.detail.current
    })
  },

  // 陪诊
  go_escort() {
    wx.navigateTo({
      url: '/pages/escort/index',
      fail(e) {
        console.log(e)
      }
    })
  },

})
