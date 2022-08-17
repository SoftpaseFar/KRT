// pages/appointment/index.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    // 医院 
    hospitals: ['中国人民解放军总医院', '医院1', '医院2', '医院3', '医院4', '医院5'],
    hospitals_index: -1,
    // 日期
    time_select: "请选择时间",
    // 科室
    departments: ['科室0', '科室1', '科室2', '科室3', '科室4', '科室5'],
    department_index: -1,
    // 就诊人
    patients_detail: [{
        "name": "蔡英文",
        "sex":"男",
        "phone_num":"13053628764",
        "id_num": "370711199898081210"
      },
      {
        "name": "测试",
        "sex":"女",
        "phone_num":"13053628766",
        "id_num": "370711199898081211"
      }
    ],


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

  form_submit(e) {
    console.log(e.detail.value);
  },
  hospitals_change(e) {
    this.setData({
      hospitals_index: e.detail.value
    });
  },

  time_change(e) {
    // console.log(e.detail.value);
    this.setData({
      time_select: e.detail.value
    });
  },

  department_change(e) {
    this.setData({
      department_index: e.detail.value
    });
  },

  go_jzr_page() {
    wx.navigateTo({
      url: '/pages/patients_detail/index',
      fail(e) {
        console.log(e)
      }
    })
  },




  // 备注
  bindinput(e) {
    this.setData({
      content: e.detail.value
    })
  },






})
