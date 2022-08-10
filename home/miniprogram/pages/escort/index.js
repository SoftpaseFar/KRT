// pages/index/index.js

const app = getApp();

let plugin = requirePlugin('routePlan');
let key = 'WM7BZ-F2JK2-LRFUO-CSYSH-XJO77-D5FXV'; //使用在腾讯位置服务申请的key
let referer = '测试'; //调用插件的app的名称
let endPoint = JSON.stringify({ //终点
  'name': '潍坊金宝游乐园',
  'latitude': 36.655792,
  'longitude': 119.126984
});

Page({


  /**
   * Page initial data
   */
  data: {
    //顶部
    top_loc_and_pub_style: "",
    search_style: "width: 50%;",

    //轮播
    background: ['https://tse2-mm.cn.bing.net/th/id/OIP-C.0-8KaD4ntl-KaJrrb-S_KQHaGO?pid=ImgDet&rs=1', 'https://img.zcool.cn/community/01b6bb579393330000018c1b442807.jpg@1280w_1l_2o_100sh.jpg', 'https://img.zcool.cn/community/013d33579393330000012e7ec25322.jpg@1280w_1l_2o_100sh.jpg'],
    indicatorDots: true,
    vertical: false,
    autoplay: true,
    interval: 2000,
    duration: 500,

    // 分类栏
    select: 0,
    height: 0,
    sortList: [
      {
        name: '陪诊',
        list: [
          {
            name: '挂号预约',
            image_url:"../../imgs/other/tengxunweibo.png",
            url:"/pages/appointment/index",
          },
          {
            name: '待取结果',
            image_url:"../../imgs/other/tengxunweibo.png",
            url:"/pages/pending_result/index",
          },
          {
            name: '带您买药',
            image_url:"../../imgs/other/tengxunweibo.png",
            url:"/pages/take_y_t_buy_med/index",
          },
          {
            name: '陪诊服务',
            image_url:"../../imgs/other/tengxunweibo.png",
            url:"/pages/escort_service/index",
          },
          {
            name: '虚位以待',
            image_url:"../../imgs/other/tengxunweibo.png",
            url:"/pages/waiting/index",
          },
        ]
      },
      {
        name: '陪护',
        list: [
          {
            name: '普通陪护',
            image_url:"../../imgs/other/tengxunweibo.png",
            url:"/pages/ordinary_escort/index",
          },
          {
            name: '专业陪护',
            image_url:"../../imgs/other/tengxunweibo.png",
            url:"/pages/professional_escort/index",
          },
          {
            name: '虚位以待',
            image_url:"../../imgs/other/tengxunweibo.png",
            url:"/pages/waiting/index",
          },

        ]
      },
    ],
    placeList: [1, 2, 3, 4]
  },

  address_plan() {
    // 跳转地图
    wx.navigateTo({
      url: 'plugin://routePlan/index?key=' + key + '&referer=' + referer + '&endPoint=' + endPoint
    });
  },

  changeType: function (e) {
    let {
      index
    } = e.currentTarget.dataset;
    if (this.data.type === index || index === undefined) {
      return false;
    } else {
      this.setData({
        nav_type: index
      })
    }

  },

  search() {
    wx.navigateTo({
      url: '/pages/historySearch/index',
      fail(e) {
        console.log(e)
      }
    })
  },
  publish() {
    wx.navigateTo({
      url: '/pages/publish/publish',
      fail(e) {
        console.log(e)
      }
    })
  },



  /**
   * Lifecycle function--Called when page load
   */
  onLoad(options) {
    this.watchHeight()
  },
  showInput(options) {
    // console.log(options);
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


  // 分类栏
  // 触发tab导航栏
  activeTab(e) {
    var index = e.currentTarget.dataset.index;
    console.log(index);
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
  enter_server_item(e){
    var item = e.currentTarget.dataset.item;
    
    wx.navigateTo({
      url: `/pages/serve/serve?item=${JSON.stringify(item)}`,
      
      fail(e) {
        console.log(e)
      }
    })
  },

  

})
