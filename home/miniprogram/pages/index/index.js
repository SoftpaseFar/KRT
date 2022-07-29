// 获取全局APP
const app = getApp();
// 转发
const db = wx.cloud.database();
// 聊天侦听器
var chatWatcher = null
// 获取计时器函数
Page({
  /**
   * 页面的初始数据
   */
  data: {
    login: false,
    //输入框距离
    InputBottom: 0,
    roomId:1,
    userInfo: {},
    content: '',
    groups: [{
      text: '点歌',
      value: 1
    }]
  },
  selectImg() {
    var that = this;
    wx.chooseImage({
      count: 1,
      sizeType: ['compressed'],
      sourceType: ['album', 'camera'],
      success: res => {
        console.log(res)
        wx.getFileSystemManager().readFile({
          filePath: res.tempFilePaths[0], //选择图片返回的相对路径
          encoding: 'base64', //编码格式
          success: res => { //成功的回调
            var bufferData = res.data;
            wx.showLoading({
              title: '信息发送',
              mask:true
            })
            wx.cloud.callFunction({
              name: 'cloud-msg-push',
              data: {
                roomId:that.data.roomId,
                msgType: 'image',
                content: bufferData
              },
              success: res => {
                console.log(res)
                if (res.result.code == 300) {
                  that.setData({
                    errMsg: res.result.msg
                  })
                }
              },
              fail: res => {
                console.log(res)
              },
              complete: res => {
                this.setData({
                  content: ''
                })
                wx.hideLoading();
              }
            })
          }
        })
      }
    })
  },
  InputFocus(e) {
    this.setData({
      InputBottom: e.detail.height
    })
  },
  InputBlur(e) {
    this.setData({
      InputBottom: 0
    })
  },
  showAction() {
    wx.showActionSheet({
      itemList: ['A', 'B', 'C'],
      success(res) {
        console.log(res.tapIndex)
      },
      fail(res) {
        console.log(res.errMsg)
      }
    })
  },
  async submit() {
    var that = this;
    if (this.data.login) {
      //已登录用户
      wx.showLoading({
        title: '信息发送',
      })
      wx.cloud.callFunction({
        name: 'cloud-msg-push',
        data: {
          roomId:that.data.roomId,
          msgType: 'text',
          content: that.data.content
        },
        success: res => {
          console.log(res)
          if (res.result.code == 300) {
            that.setData({
              errMsg: res.result.msg
            })
          }

          console.log(res)
        },
        fail: res => {
          console.log(res)
        },
        complete: res => {
          this.setData({
            content: ''
          })
          wx.hideLoading();
        }
      })
    } else {
      // 
      wx.getUserProfile({
        desc: '获取用户聊天头像',
        success: res => {
          // console.log(res)
          let userInfo = res.userInfo
          //
          wx.showLoading({
            title: '获取用户信息',
          })
          this.userRegister(userInfo).then(r => {
            console.log(r)
            wx.hideLoading();
            that.setData({
              login: true
            }, () => {
              that.submit();
            })
          })
        }
      })
    }
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.userAuth();
  },
  userRegister(userInfo) {
    return new Promise(function (resolve, reject) {
      wx.cloud.callFunction({
        name: 'cloud-user',
        data: {
          userInfo: userInfo
        },
        success: res => {
          resolve(res)

        },
        fail: res => {
          reject(res)
        }
      })
    })

  },
  userAuth() {
    //身份校验
    wx.cloud.callFunction({
      name: 'auth',
      success: res => {
        console.log(res)

        if (res.result.errCode == -1) {
          //
          console.log('--未登录--')
          this.setData({
            login: false
          })
        } else {
          console.log('--已登录--')
          this.setData({
            login: true
          })
        }
      },
      fail: res => {
        console.log(res)
      }
    })
  },
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})