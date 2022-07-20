// pages/index/index.js

const app = getApp()

Page({


  /**
   * Page initial data
   */
  data: {
    //顶部
    top_loc_and_pub_style:"",
    search_style:"width: 50%;",

    //轮播
    background: ['https://tse2-mm.cn.bing.net/th/id/OIP-C.0-8KaD4ntl-KaJrrb-S_KQHaGO?pid=ImgDet&rs=1', 'https://img.zcool.cn/community/01b6bb579393330000018c1b442807.jpg@1280w_1l_2o_100sh.jpg', 'https://img.zcool.cn/community/013d33579393330000012e7ec25322.jpg@1280w_1l_2o_100sh.jpg'],
    indicatorDots: true,
    vertical: false,
    autoplay: true,
    interval: 2000,
    duration: 500,

    //搜索框
    inputShowed: false, //初始文本框不显示内容

    //分类栏
    select: 0,
    height: 0,
    sortList: [{
        name: '门诊陪诊'
      },
      {
        name: '校园生活'
      },
      {
        name: '紧急帮助'
      },
      {
        name: '特色服务'
      },
      {
        name: '传统服务'
      },
      /*
      {
        name: '服务1'
      },
      {
        name: '服务2'
      },
      {
        name: '服务3'
      },
      {
        name: '服务5'
      },*/
    ],
    placeList: [1, 2, 3, 4]



  },


  // 使文本框进入可编辑状态
  showInput: function () {
    this.setData({
      inputShowed: true, //设置文本框可以输入内容
      top_loc_and_pub_style:"display: none;",
      search_style:"width: 100%;",
    });
  },
  // 取消搜索
  hideInput: function () {
    this.setData({
      inputShowed: false,
      top_loc_and_pub_style:"",
      search_style:"width: 50%;",
    });
  },


  /**
   * Lifecycle function--Called when page load
   */
  onLoad(options) {
    //分类栏
    this.watchHeight()
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



  //分类专栏
  // 触发tab导航栏
  activeTab(e) {
    var index = e.currentTarget.dataset.index
    this.setData({
      select: index
    })
    this.generalEv()
    this.watchHeight()
  },

  // 滑动swiper
  activeSw(e) {
    var index = e.detail.current
    this.setData({
      select: index
    })
    this.generalEv()
    this.watchHeight()
  },

  // 监听swiper高度
  watchHeight() {
    var query = wx.createSelectorQuery()
    query.select('.box').boundingClientRect((res) => {
      this.setData({
        height: parseInt(res.height)
      })
    }).exec()
  },

  // 初始化值
  generalEv() {
    this.setData({
      placeList: [1, 2, 3, 4]
    })
    // 回到顶部
    wx.pageScrollTo({
      scrollTop: 0
    })
  },

  onReachBottom: function () {
    var list = this.data.placeList
    list.push(1, 2, 3, 4)
    this.setData({
      placeList: list
    })
    this.watchHeight()
  },


})
