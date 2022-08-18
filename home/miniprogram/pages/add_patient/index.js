// pages/add_patient/index.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    radio_select: ['男', '女'],

    patients_detail: [],
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    var patients_detail = JSON.parse(options.data);
    this.setData({
      patients_detail: patients_detail
    });
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

  form_submit(e) {
    var form_info = e.detail.value;

    var patients_detail = this.data.patients_detail;

    patients_detail.push({
      "name": form_info.name,
      "sex": form_info.sex,
      "phone_num": form_info.phone_num,
      "id_num": form_info.id_num,
      "selected": false,
      "status": true
    });

    var pages = getCurrentPages(); //当前页面
    var beforePage = pages[pages.length - 2]; //前一页



    beforePage.setData({
      back_code: 1,
      patients_detail: patients_detail,
    });
    beforePage.onLoad(); // 执行前一个页面的onLoad方法
    wx.navigateBack({
      delta: 1
    });
  },
})
