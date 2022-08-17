Page({

  /**
   * 页面的初始数据
   */
  data: {
    calculation: 0,
    selectAllStatus: false,
    startX: '',
    startY: '',
    effective_carts: [], // 有效列表
    patients_detail: [{
        "name": "蔡英文",
        "sex": "女",
        "phone_num": "13053628764",
        "id_num": "370711199898081210",
        "selected": false,
        "status": true
      },
      {
        "name": "测试",
        "sex": "男",
        "phone_num": "13053628766",
        "id_num": "370711199898081211",
        "selected": false,
        "status": true
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
  selectList(e) {
    let idx = parseInt(e.currentTarget.dataset.index);
    var patients_detail = this.data.patients_detail;
    patients_detail[idx]['selected'] = !patients_detail[idx]['selected'];

    var calculation = this.data.calculation;


    if (patients_detail[idx]['selected']) {
      calculation = calculation + 1;
    } else {
      calculation = calculation - 1;
    }
    if (calculation == patients_detail.length) {
      this.setData({
        selectAllStatus: true,
        calculation: calculation,
        patients_detail: patients_detail
      });
    } else {
      this.setData({
        selectAllStatus: false,
        calculation: calculation,
        patients_detail: patients_detail
      });
    }


  },



  //触摸开始
  touchS(e) {
    for (let key in this.data.patients_detail) {
      this.data.patients_detail[key]['status'] = true;
    }
    this.setData({
      patients_detail: this.data.patients_detail,
    })
    // 获得起始坐标
    this.data.startX = e.touches[0].clientX;
    this.data.startY = e.touches[0].clientY;
  },

  //滑动
  touchM(e) {
    // 获得当前坐标
    var currentX = e.touches[0].clientX;
    var currentY = e.touches[0].clientY;
    const x = this.data.startX - currentX; //横向移动距离
    const y = Math.abs(this.data.startY - currentY); //纵向移动距离，若向左移动有点倾斜也可以接受
    var id = e.currentTarget.dataset.index;
    for (let key in this.data.effective_carts) {
      if (key == id) {
        if (x > 35 && y < 110) {
          //向左滑是显示删除
          this.data.effective_carts[key]['status'] = false;
        } else if (x < -35 && y < 110) {
          //向右滑
          this.data.effective_carts[key]['status'] = true;
        }
      }
    }
    this.setData({
      effective_carts: this.data.effective_carts,
    })
  },

  selectAll() {
    var patients_detail = this.data.patients_detail;
    var calculation = 0;
    if (!this.data.selectAllStatus) {
      calculation = patients_detail.length;
      patients_detail.forEach(function (item) {
        item.selected = true;
      })
    } else {
      patients_detail.forEach(function (item) {
        item.selected = false;
      })
    }


    this.setData({
      calculation: calculation,
      patients_detail: patients_detail,
      selectAllStatus: !this.data.selectAllStatus
    });
  },





  //触摸开始
  touchS(e) {
    for (let key in this.data.patients_detail) {
      this.data.patients_detail[key]['status'] = true;
    }
    this.setData({
      patients_detail: this.data.patients_detail,
    })
    // 获得起始坐标
    this.data.startX = e.touches[0].clientX;
    this.data.startY = e.touches[0].clientY;
  },
  //滑动
  touchM(e) {
    // 获得当前坐标
    var currentX = e.touches[0].clientX;
    var currentY = e.touches[0].clientY;
    const x = this.data.startX - currentX; //横向移动距离
    const y = Math.abs(this.data.startY - currentY); //纵向移动距离，若向左移动有点倾斜也可以接受
    var id = e.currentTarget.dataset.index;
    for (let key in this.data.patients_detail) {
      if (key == id) {
        if (x > 35 && y < 110) {
          //向左滑是显示删除
          this.data.patients_detail[key]['status'] = false;
        } else if (x < -35 && y < 110) {
          //向右滑
          this.data.patients_detail[key]['status'] = true;
        }
      }
    }
    this.setData({
      patients_detail: this.data.patients_detail,
    })
  },


  deleteList(e) {
    // console.log(11);

    let idx = parseInt(e.currentTarget.dataset.index);
    var patients_detail = this.data.patients_detail;
    var calculation = this.data.calculation;
    if (patients_detail[idx]['selected']) {
      calculation = calculation - 1;
    }

    patients_detail.splice(idx, 1);



    this.setData({
      calculation: calculation,
      patients_detail: patients_detail
    })
  },


})
