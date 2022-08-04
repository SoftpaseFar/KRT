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
    sortList: [{
        name: '门诊陪诊',
        list: [{
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试13', '测试1', '测试13', '测试11', '测试123'],
            salary: 1000,
            address: "山东省日照市东港区",
          },
          {
            name: '接送孩子',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试12', '测试12', '测试12', '测试12', '测试12'],
            salary: 1000,
            address: "山东省日照市东港区",
          },
          {
            name: '网络培训',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试1', '测试1', '测试1', '测试1', '测试1'],
            salary: 1000,
            address: "山东省日照市东港区",
          },
          {
            name: '帮拿快递',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试1', '测试1', '测试1', '测试1', '测试1'],
            salary: 1000,
            address: "山东省日照市东港区",
          },
          {
            name: '测试',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试1', '测试1', '测试1', '测试1', '测试1'],
            salary: 1000,
            address: "山东省日照市东港区",
          },
          {
            name: '测试一',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试1', '测试1', '测试1', '测试1', '测试1'],
            salary: 1000,
            address: "山东省日照市东港区",
          },
          {
            name: '辅导作业1',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试1', '测试1', '测试1', '测试1', '测试1'],
            salary: 1000,
            address: "山东省日照市东港区",
          },
          {
            name: '辅导作业2',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试1', '测试1', '测试1', '测试1', '测试1'],
            salary: 1000,
            address: "山东省日照市东港区",
          },
          {
            name: '辅导作业3',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试1', '测试1', '测试1', '测试1', '测试1'],
            salary: 1000,
            address: "山东省日照市东港区",
          },
        ]
      },
      {
        name: '校园生活',
        list: [{
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试1', '测试1', '测试1', '测试1', '测试1'],
            salary: 2000,
            address: "山东省日照市东港区1",
          },
          {
            name: '接送孩子',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试1', '测试1', '测试1', '测试1', '测试1'],
            salary: 2000,
            address: "山东省日照市东港区1",
          },
          {
            name: '快递服务',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试1', '测试1', '测试1', '测试1', '测试1'],
            salary: 2000,
            address: "山东省日照市东港区1",
          },
          {
            name: '网络培训',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试1', '测试1', '测试1', '测试1', '测试1'],
            salary: 2000,
            address: "山东省日照市东港区1",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试1', '测试1', '测试1', '测试1', '测试1'],
            salary: 2000,
            address: "山东省日照市东港区1",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试1', '测试1', '测试1', '测试1', '测试1'],
            salary: 2000,
            address: "山东省日照市东港区1",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试1', '测试1', '测试1', '测试1', '测试1'],
            salary: 2000,
            address: "山东省日照市东港区1",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试1', '测试1', '测试1', '测试1', '测试1'],
            salary: 2000,
            address: "山东省日照市东港区1",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试1', '测试1', '测试1', '测试1', '测试1'],
            salary: 2000,
            address: "山东省日照市东港区1",
          },
        ]
      },
      {
        name: '紧急帮助',
        list: [{
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试1', '测试1', '测试1', '测试1', '测试1'],
            salary: 2000,
            address: "山东省日照市东港区1",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试1', '测试1', '测试1', '测试1', '测试1'],
            salary: 2000,
            address: "山东省日照市东港区1",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试1', '测试1', '测试1', '测试1', '测试1'],
            salary: 2000,
            address: "山东省日照市东港区1",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试1', '测试1', '测试1', '测试1', '测试1'],
            salary: 2000,
            address: "山东省日照市东港区1",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试1', '测试1', '测试1', '测试1', '测试1'],
            salary: 2000,
            address: "山东省日照市东港区1",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试1', '测试1', '测试1', '测试1', '测试1'],
            salary: 2000,
            address: "山东省日照市东港区1",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试1', '测试1', '测试1', '测试1', '测试1'],
            salary: 2000,
            address: "山东省日照市东港区1",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试1', '测试1', '测试1', '测试1', '测试1'],
            salary: 2000,
            address: "山东省日照市东港区1",
          },
        ]
      },
      {
        name: '特色服务',
        list: [{
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试2', '测试12', '测试21', '测试21', '测试21'],
            salary: 3000,
            address: "山东省日照市东港区3",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试2', '测试12', '测试21', '测试21', '测试21'],
            salary: 3000,
            address: "山东省日照市东港区3",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试2', '测试12', '测试21', '测试21', '测试21'],
            salary: 3000,
            address: "山东省日照市东港区3",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试2', '测试12', '测试21', '测试21', '测试21'],
            salary: 3000,
            address: "山东省日照市东港区3",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试2', '测试12', '测试21', '测试21', '测试21'],
            salary: 3000,
            address: "山东省日照市东港区3",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试2', '测试12', '测试21', '测试21', '测试21'],
            salary: 3000,
            address: "山东省日照市东港区3",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试2', '测试12', '测试21', '测试21', '测试21'],
            salary: 3000,
            address: "山东省日照市东港区3",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试2', '测试12', '测试21', '测试21', '测试21'],
            salary: 3000,
            address: "山东省日照市东港区3",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试2', '测试12', '测试21', '测试21', '测试21'],
            salary: 3000,
            address: "山东省日照市东港区3",
          },
        ]
      },
      {
        name: '传统服务',
        list: [{
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试23', '测试132', '测试231', '测试231', '测试231'],
            salary: 3000,
            address: "山东省日照市东港区3",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试23', '测试132', '测试231', '测试231', '测试231'],
            salary: 3000,
            address: "山东省日照市东港区3",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试23', '测试132', '测试231', '测试231', '测试231'],
            salary: 3000,
            address: "山东省日照市东港区3",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试23', '测试132', '测试231', '测试231', '测试231'],
            salary: 3000,
            address: "山东省日照市东港区3",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试23', '测试132', '测试231', '测试231', '测试231'],
            salary: 3000,
            address: "山东省日照市东港区3",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试23', '测试132', '测试231', '测试231', '测试231'],
            salary: 3000,
            address: "山东省日照市东港区3",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试23', '测试132', '测试231', '测试231', '测试231'],
            salary: 3000,
            address: "山东省日照市东港区3",
          },
          {
            name: '辅导作业',
            time: "2022.9.1",
            duration: '一星期',
            required: '90',
            registered: '60',
            label: ['测试23', '测试132', '测试231', '测试231', '测试231'],
            salary: 3000,
            address: "山东省日照市东港区3",
          }
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




})
