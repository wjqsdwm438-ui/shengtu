import type {Rect} from "../ql01-pilot/feather-mask";

export type LayerConfig = {readonly id: string; readonly name: string; readonly rects: readonly Rect[]};
export type PageConfig = {readonly page: string; readonly source: string; readonly layers: readonly LayerConfig[]; readonly combinedRects?: readonly Rect[]; readonly combinedFeathers?: readonly number[]};

export const pageConfigs = [
  {
    "page": "QL-02",
    "source": "ql-batch/QL-02.png",
    "layers": [
      {
        "id": "QL-02-L01",
        "name": "收货场景",
        "rects": [
          {
            "x": 130,
            "y": 220,
            "width": 790,
            "height": 725
          },
          {
            "x": 130,
            "y": 180,
            "width": 420,
            "height": 80
          }
        ]
      },
      {
        "id": "QL-02-L02",
        "name": "定义文字",
        "rects": [
          {
            "x": 940,
            "y": 275,
            "width": 850,
            "height": 390
          }
        ]
      },
      {
        "id": "QL-02-L03",
        "name": "核心边界",
        "rects": [
          {
            "x": 940,
            "y": 690,
            "width": 830,
            "height": 120
          }
        ]
      }
    ],
    "combinedRects": [
      {
        "x": 130,
        "y": 220,
        "width": 790,
        "height": 725
      },
      {
        "x": 130,
        "y": 180,
        "width": 420,
        "height": 80
      },
      {
        "x": 940,
        "y": 275,
        "width": 850,
        "height": 390
      },
      {
        "x": 940,
        "y": 690,
        "width": 830,
        "height": 120
      }
    ],
    "combinedFeathers": [
      18,
      18,
      18,
      18
    ]
  },
  {
    "page": "QL-03",
    "source": "ql-batch/QL-03.png",
    "layers": [
      {
        "id": "QL-03-L01",
        "name": "五步作业链",
        "rects": [
          {
            "x": 145,
            "y": 275,
            "width": 1645,
            "height": 535
          }
        ]
      },
      {
        "id": "QL-03-L02",
        "name": "结果",
        "rects": [
          {
            "x": 285,
            "y": 850,
            "width": 1350,
            "height": 105
          }
        ]
      }
    ],
    "combinedRects": [
      {
        "x": 145,
        "y": 275,
        "width": 1645,
        "height": 535
      },
      {
        "x": 285,
        "y": 850,
        "width": 1350,
        "height": 105
      }
    ],
    "combinedFeathers": [
      18,
      2
    ]
  },
  {
    "page": "QL-04",
    "source": "ql-batch/QL-04.png",
    "layers": [
      {
        "id": "QL-04-L01",
        "name": "盲目采购",
        "rects": [
          {
            "x": 165,
            "y": 195,
            "width": 795,
            "height": 390
          }
        ]
      },
      {
        "id": "QL-04-L02",
        "name": "物资积压",
        "rects": [
          {
            "x": 960,
            "y": 195,
            "width": 795,
            "height": 390
          }
        ]
      },
      {
        "id": "QL-04-L03",
        "name": "物料短缺",
        "rects": [
          {
            "x": 165,
            "y": 580,
            "width": 795,
            "height": 390
          }
        ]
      },
      {
        "id": "QL-04-L04",
        "name": "验收低效",
        "rects": [
          {
            "x": 960,
            "y": 580,
            "width": 795,
            "height": 390
          }
        ]
      }
    ],
    "combinedRects": [
      {
        "x": 165,
        "y": 195,
        "width": 1590,
        "height": 775
      }
    ],
    "combinedFeathers": [
      10
    ]
  },
  {
    "page": "QL-05",
    "source": "ql-batch/QL-05.png",
    "layers": [
      {
        "id": "QL-05-L01",
        "name": "供应协同完整场景",
        "rects": [
          {
            "x": 180,
            "y": 210,
            "width": 1595,
            "height": 665
          }
        ]
      },
      {
        "id": "QL-05-L02",
        "name": "结果",
        "rects": [
          {
            "x": 240,
            "y": 875,
            "width": 1485,
            "height": 80
          }
        ]
      }
    ],
    "combinedRects": [
      {
        "x": 180,
        "y": 210,
        "width": 1595,
        "height": 745
      }
    ],
    "combinedFeathers": [
      10
    ]
  },
  {
    "page": "QL-06",
    "source": "ql-batch/QL-06.png",
    "layers": [
      {
        "id": "QL-06-L01",
        "name": "核心口诀图文",
        "rects": [
          {
            "x": 250,
            "y": 260,
            "width": 1440,
            "height": 600
          },
          {
            "x": 1240,
            "y": 500,
            "width": 570,
            "height": 420
          }
        ]
      }
    ]
  },
  {
    "page": "QL-07",
    "source": "ql-batch/QL-07.png",
    "layers": [
      {
        "id": "QL-07-L01",
        "name": "企业内部说明",
        "rects": [
          {
            "x": 550,
            "y": 205,
            "width": 820,
            "height": 85
          }
        ]
      },
      {
        "id": "QL-07-L02",
        "name": "原料仓出库",
        "rects": [
          {
            "x": 80,
            "y": 300,
            "width": 320,
            "height": 390
          }
        ]
      },
      {
        "id": "QL-07-L03",
        "name": "搬运",
        "rects": [
          {
            "x": 360,
            "y": 300,
            "width": 310,
            "height": 390
          }
        ]
      },
      {
        "id": "QL-07-L04",
        "name": "工序流转",
        "rects": [
          {
            "x": 630,
            "y": 300,
            "width": 340,
            "height": 390
          }
        ]
      },
      {
        "id": "QL-07-L05",
        "name": "半成品暂存",
        "rects": [
          {
            "x": 920,
            "y": 300,
            "width": 340,
            "height": 390
          }
        ]
      },
      {
        "id": "QL-07-L06",
        "name": "组装",
        "rects": [
          {
            "x": 1210,
            "y": 300,
            "width": 340,
            "height": 390
          }
        ]
      },
      {
        "id": "QL-07-L07",
        "name": "成品入库",
        "rects": [
          {
            "x": 1500,
            "y": 300,
            "width": 340,
            "height": 390
          }
        ]
      },
      {
        "id": "QL-07-L08",
        "name": "路线层",
        "rects": [
          {
            "x": 335,
            "y": 585,
            "width": 95,
            "height": 115
          },
          {
            "x": 620,
            "y": 585,
            "width": 95,
            "height": 115
          },
          {
            "x": 910,
            "y": 585,
            "width": 95,
            "height": 115
          },
          {
            "x": 1200,
            "y": 585,
            "width": 95,
            "height": 115
          },
          {
            "x": 1490,
            "y": 585,
            "width": 95,
            "height": 115
          }
        ]
      },
      {
        "id": "QL-07-L09",
        "name": "底部定义",
        "rects": [
          {
            "x": 80,
            "y": 745,
            "width": 1000,
            "height": 175
          }
        ]
      },
      {
        "id": "QL-07-L10",
        "name": "价值结论",
        "rects": [
          {
            "x": 1080,
            "y": 745,
            "width": 760,
            "height": 175
          }
        ]
      }
    ]
  },
  {
    "page": "QL-08",
    "source": "ql-batch/QL-08.png",
    "layers": [
      {
        "id": "QL-08-L01",
        "name": "库存原料按需出库",
        "rects": [
          {
            "x": 170,
            "y": 215,
            "width": 520,
            "height": 330
          }
        ]
      },
      {
        "id": "QL-08-L02",
        "name": "车间智能转运",
        "rects": [
          {
            "x": 700,
            "y": 215,
            "width": 520,
            "height": 330
          }
        ]
      },
      {
        "id": "QL-08-L03",
        "name": "各工序加工流转",
        "rects": [
          {
            "x": 1230,
            "y": 215,
            "width": 520,
            "height": 330
          }
        ]
      },
      {
        "id": "QL-08-L04",
        "name": "半成品临时仓储",
        "rects": [
          {
            "x": 170,
            "y": 545,
            "width": 520,
            "height": 390
          }
        ]
      },
      {
        "id": "QL-08-L05",
        "name": "成品组装质检",
        "rects": [
          {
            "x": 700,
            "y": 545,
            "width": 520,
            "height": 390
          }
        ]
      },
      {
        "id": "QL-08-L06",
        "name": "成品入库",
        "rects": [
          {
            "x": 1230,
            "y": 545,
            "width": 520,
            "height": 390
          }
        ]
      }
    ],
    "combinedRects": [
      {
        "x": 170,
        "y": 215,
        "width": 1580,
        "height": 720
      }
    ],
    "combinedFeathers": [
      10
    ]
  },
  {
    "page": "QL-09",
    "source": "ql-batch/QL-09.png",
    "layers": [
      {
        "id": "QL-09-L01",
        "name": "动线混乱",
        "rects": [
          {
            "x": 155,
            "y": 220,
            "width": 390,
            "height": 650
          }
        ]
      },
      {
        "id": "QL-09-L02",
        "name": "物料堆积",
        "rects": [
          {
            "x": 555,
            "y": 220,
            "width": 380,
            "height": 650
          }
        ]
      },
      {
        "id": "QL-09-L03",
        "name": "人工搬运低效",
        "rects": [
          {
            "x": 945,
            "y": 220,
            "width": 380,
            "height": 650
          }
        ]
      },
      {
        "id": "QL-09-L04",
        "name": "工序衔接断层",
        "rects": [
          {
            "x": 1335,
            "y": 220,
            "width": 420,
            "height": 650
          }
        ]
      },
      {
        "id": "QL-09-L05",
        "name": "结果",
        "rects": [
          {
            "x": 480,
            "y": 875,
            "width": 1000,
            "height": 80
          }
        ]
      }
    ],
    "combinedRects": [
      {
        "x": 155,
        "y": 220,
        "width": 1600,
        "height": 735
      }
    ],
    "combinedFeathers": [
      2
    ]
  },
  {
    "page": "QL-10",
    "source": "ql-batch/QL-10.png",
    "layers": [
      {
        "id": "QL-10-L01",
        "name": "AGV搬运机器人",
        "rects": [
          {
            "x": 160,
            "y": 210,
            "width": 520,
            "height": 650
          }
        ]
      },
      {
        "id": "QL-10-L02",
        "name": "智能动线规划",
        "rects": [
          {
            "x": 695,
            "y": 210,
            "width": 525,
            "height": 650
          }
        ]
      },
      {
        "id": "QL-10-L03",
        "name": "数字化生产调度",
        "rects": [
          {
            "x": 1235,
            "y": 210,
            "width": 530,
            "height": 650
          }
        ]
      },
      {
        "id": "QL-10-L04",
        "name": "结果",
        "rects": [
          {
            "x": 330,
            "y": 875,
            "width": 1260,
            "height": 75
          }
        ]
      }
    ],
    "combinedRects": [
      {
        "x": 160,
        "y": 210,
        "width": 1605,
        "height": 740
      }
    ],
    "combinedFeathers": [
      10
    ]
  },
  {
    "page": "QL-11",
    "source": "ql-batch/QL-11.png",
    "layers": [
      {
        "id": "QL-11-L01",
        "name": "核心口诀图文",
        "rects": [
          {
            "x": 210,
            "y": 250,
            "width": 1520,
            "height": 640
          }
        ]
      }
    ]
  },
  {
    "page": "QL-12",
    "source": "ql-batch/QL-12.png",
    "layers": [
      {
        "id": "QL-12-L01",
        "name": "业务场景",
        "rects": [
          {
            "x": 130,
            "y": 220,
            "width": 1000,
            "height": 725
          }
        ]
      },
      {
        "id": "QL-12-L02",
        "name": "定义文字",
        "rects": [
          {
            "x": 1135,
            "y": 280,
            "width": 640,
            "height": 380
          }
        ]
      },
      {
        "id": "QL-12-L03",
        "name": "核心价值",
        "rects": [
          {
            "x": 1135,
            "y": 685,
            "width": 640,
            "height": 255
          }
        ]
      }
    ]
  },
  {
    "page": "QL-13",
    "source": "ql-batch/QL-13.png",
    "layers": [
      {
        "id": "QL-13-L01",
        "name": "接收客户订单",
        "rects": [
          {
            "x": 205,
            "y": 235,
            "width": 480,
            "height": 325
          }
        ]
      },
      {
        "id": "QL-13-L02",
        "name": "成品拣货打包",
        "rects": [
          {
            "x": 730,
            "y": 235,
            "width": 475,
            "height": 325
          }
        ]
      },
      {
        "id": "QL-13-L03",
        "name": "智能分拣出库",
        "rects": [
          {
            "x": 1260,
            "y": 235,
            "width": 470,
            "height": 325
          }
        ]
      },
      {
        "id": "QL-13-L04",
        "name": "干线运输或同城配送",
        "rects": [
          {
            "x": 205,
            "y": 565,
            "width": 480,
            "height": 320
          }
        ]
      },
      {
        "id": "QL-13-L05",
        "name": "终端交付签收",
        "rects": [
          {
            "x": 730,
            "y": 565,
            "width": 475,
            "height": 320
          }
        ]
      },
      {
        "id": "QL-13-L06",
        "name": "订单闭环",
        "rects": [
          {
            "x": 1260,
            "y": 565,
            "width": 470,
            "height": 320
          }
        ]
      },
      {
        "id": "QL-13-L07",
        "name": "客户体验结论",
        "rects": [
          {
            "x": 215,
            "y": 890,
            "width": 1510,
            "height": 60
          }
        ]
      }
    ],
    "combinedRects": [
      {
        "x": 190,
        "y": 245,
        "width": 1560,
        "height": 700
      }
    ],
    "combinedFeathers": [
      10
    ]
  },
  {
    "page": "QL-14",
    "source": "ql-batch/QL-14.png",
    "layers": [
      {
        "id": "QL-14-L01",
        "name": "人工分拣低效",
        "rects": [
          {
            "x": 155,
            "y": 210,
            "width": 390,
            "height": 635
          }
        ]
      },
      {
        "id": "QL-14-L02",
        "name": "配送时效不稳",
        "rects": [
          {
            "x": 545,
            "y": 210,
            "width": 395,
            "height": 635
          }
        ]
      },
      {
        "id": "QL-14-L03",
        "name": "订单轨迹不透明",
        "rects": [
          {
            "x": 935,
            "y": 210,
            "width": 405,
            "height": 635
          }
        ]
      },
      {
        "id": "QL-14-L04",
        "name": "错发漏发",
        "rects": [
          {
            "x": 1335,
            "y": 210,
            "width": 425,
            "height": 635
          }
        ]
      },
      {
        "id": "QL-14-L05",
        "name": "结果",
        "rects": [
          {
            "x": 160,
            "y": 860,
            "width": 1600,
            "height": 80
          }
        ]
      }
    ],
    "combinedRects": [
      {
        "x": 155,
        "y": 210,
        "width": 1605,
        "height": 730
      }
    ],
    "combinedFeathers": [
      10
    ]
  },
  {
    "page": "QL-15",
    "source": "ql-batch/QL-15.png",
    "layers": [
      {
        "id": "QL-15-L01",
        "name": "TMS统一运输调度",
        "rects": [
          {
            "x": 155,
            "y": 200,
            "width": 770,
            "height": 330
          }
        ]
      },
      {
        "id": "QL-15-L02",
        "name": "智能分拣设备",
        "rects": [
          {
            "x": 935,
            "y": 200,
            "width": 815,
            "height": 330
          }
        ]
      },
      {
        "id": "QL-15-L03",
        "name": "AI路径规划",
        "rects": [
          {
            "x": 155,
            "y": 535,
            "width": 770,
            "height": 335
          }
        ]
      },
      {
        "id": "QL-15-L04",
        "name": "可视化追踪",
        "rects": [
          {
            "x": 935,
            "y": 535,
            "width": 815,
            "height": 335
          }
        ]
      },
      {
        "id": "QL-15-L05",
        "name": "结果",
        "rects": [
          {
            "x": 170,
            "y": 880,
            "width": 1580,
            "height": 75
          }
        ]
      }
    ],
    "combinedRects": [
      {
        "x": 155,
        "y": 200,
        "width": 1595,
        "height": 755
      }
    ],
    "combinedFeathers": [
      2
    ]
  },
  {
    "page": "QL-16",
    "source": "ql-batch/QL-16.png",
    "layers": [
      {
        "id": "QL-16-L01",
        "name": "上部口诀",
        "rects": [
          {
            "x": 215,
            "y": 220,
            "width": 1495,
            "height": 265
          }
        ]
      },
      {
        "id": "QL-16-L02",
        "name": "下部MG场景",
        "rects": [
          {
            "x": 130,
            "y": 500,
            "width": 1040,
            "height": 445
          }
        ]
      },
      {
        "id": "QL-16-L03",
        "name": "解释文字",
        "rects": [
          {
            "x": 1185,
            "y": 545,
            "width": 530,
            "height": 390
          }
        ]
      }
    ]
  },
  {
    "page": "QL-17",
    "source": "ql-batch/QL-17.png",
    "layers": [
      {
        "id": "QL-17-L01",
        "name": "回收业务场景",
        "rects": [
          {
            "x": 180,
            "y": 220,
            "width": 750,
            "height": 690
          }
        ]
      },
      {
        "id": "QL-17-L02",
        "name": "定义文字",
        "rects": [
          {
            "x": 925,
            "y": 220,
            "width": 790,
            "height": 150
          }
        ]
      },
      {
        "id": "QL-17-L03",
        "name": "五类对象组",
        "rects": [
          {
            "x": 925,
            "y": 350,
            "width": 790,
            "height": 290
          }
        ]
      },
      {
        "id": "QL-17-L04",
        "name": "职责结论",
        "rects": [
          {
            "x": 925,
            "y": 645,
            "width": 790,
            "height": 265
          }
        ]
      }
    ],
    "combinedRects": [
      {
        "x": 180,
        "y": 220,
        "width": 1535,
        "height": 690
      }
    ],
    "combinedFeathers": [
      18
    ]
  },
  {
    "page": "QL-18",
    "source": "ql-batch/QL-18.png",
    "layers": [
      {
        "id": "QL-18-L01",
        "name": "三步处置主线",
        "rects": [
          {
            "x": 180,
            "y": 220,
            "width": 1540,
            "height": 200
          }
        ]
      },
      {
        "id": "QL-18-L02",
        "name": "完好商品重新入库",
        "rects": [
          {
            "x": 180,
            "y": 430,
            "width": 770,
            "height": 190
          }
        ]
      },
      {
        "id": "QL-18-L03",
        "name": "瑕疵商品维修复用",
        "rects": [
          {
            "x": 960,
            "y": 430,
            "width": 770,
            "height": 190
          }
        ]
      },
      {
        "id": "QL-18-L04",
        "name": "破损商品合规报废",
        "rects": [
          {
            "x": 180,
            "y": 625,
            "width": 770,
            "height": 190
          }
        ]
      },
      {
        "id": "QL-18-L05",
        "name": "生产废料回收再利用",
        "rects": [
          {
            "x": 960,
            "y": 625,
            "width": 770,
            "height": 190
          }
        ]
      },
      {
        "id": "QL-18-L06",
        "name": "关键动作",
        "rects": [
          {
            "x": 180,
            "y": 820,
            "width": 1540,
            "height": 125
          }
        ]
      }
    ],
    "combinedRects": [
      {
        "x": 180,
        "y": 220,
        "width": 1540,
        "height": 715
      }
    ],
    "combinedFeathers": [
      10
    ]
  },
  {
    "page": "QL-19",
    "source": "ql-batch/QL-19.png",
    "layers": [
      {
        "id": "QL-19-L01",
        "name": "流程混乱",
        "rects": [
          {
            "x": 160,
            "y": 210,
            "width": 510,
            "height": 500
          }
        ]
      },
      {
        "id": "QL-19-L02",
        "name": "处理缓慢",
        "rects": [
          {
            "x": 690,
            "y": 210,
            "width": 520,
            "height": 500
          }
        ]
      },
      {
        "id": "QL-19-L03",
        "name": "资源浪费",
        "rects": [
          {
            "x": 1240,
            "y": 210,
            "width": 520,
            "height": 500
          }
        ]
      },
      {
        "id": "QL-19-L04",
        "name": "经营后果",
        "rects": [
          {
            "x": 155,
            "y": 720,
            "width": 1605,
            "height": 100
          }
        ]
      },
      {
        "id": "QL-19-L05",
        "name": "共同根因",
        "rects": [
          {
            "x": 155,
            "y": 830,
            "width": 1605,
            "height": 100
          }
        ]
      }
    ],
    "combinedRects": [
      {
        "x": 155,
        "y": 210,
        "width": 1605,
        "height": 720
      }
    ],
    "combinedFeathers": [
      10
    ]
  },
  {
    "page": "QL-20",
    "source": "ql-batch/QL-20.png",
    "layers": [
      {
        "id": "QL-20-L01",
        "name": "平台底座",
        "rects": [
          {
            "x": 145,
            "y": 210,
            "width": 1630,
            "height": 245
          }
        ]
      },
      {
        "id": "QL-20-L02",
        "name": "全程溯源",
        "rects": [
          {
            "x": 145,
            "y": 450,
            "width": 525,
            "height": 390
          }
        ]
      },
      {
        "id": "QL-20-L03",
        "name": "智能质检",
        "rects": [
          {
            "x": 695,
            "y": 450,
            "width": 525,
            "height": 390
          }
        ]
      },
      {
        "id": "QL-20-L04",
        "name": "自动回仓",
        "rects": [
          {
            "x": 1245,
            "y": 450,
            "width": 530,
            "height": 390
          }
        ]
      },
      {
        "id": "QL-20-L05",
        "name": "结果",
        "rects": [
          {
            "x": 145,
            "y": 855,
            "width": 1630,
            "height": 130
          }
        ]
      }
    ],
    "combinedRects": [
      {
        "x": 145,
        "y": 210,
        "width": 1630,
        "height": 775
      }
    ],
    "combinedFeathers": [
      10
    ]
  },
  {
    "page": "QL-21",
    "source": "ql-batch/QL-21.png",
    "layers": [
      {
        "id": "QL-21-L01",
        "name": "主口诀文字",
        "rects": [
          {
            "x": 180,
            "y": 250,
            "width": 850,
            "height": 345
          }
        ]
      },
      {
        "id": "QL-21-L02",
        "name": "三行处置文字",
        "rects": [
          {
            "x": 180,
            "y": 580,
            "width": 750,
            "height": 340
          }
        ]
      },
      {
        "id": "QL-21-L03",
        "name": "右侧MG场景",
        "rects": [
          {
            "x": 1020,
            "y": 225,
            "width": 820,
            "height": 330
          },
          {
            "x": 950,
            "y": 500,
            "width": 890,
            "height": 435
          }
        ]
      }
    ],
    "combinedRects": [
      {
        "x": 180,
        "y": 225,
        "width": 1660,
        "height": 710
      }
    ],
    "combinedFeathers": [
      18
    ]
  },
  {
    "page": "QL-22",
    "source": "ql-batch/QL-22.png",
    "layers": [
      {
        "id": "QL-22-L01",
        "name": "供应物流",
        "rects": [
          {
            "x": 165,
            "y": 210,
            "width": 405,
            "height": 635
          }
        ]
      },
      {
        "id": "QL-22-L02",
        "name": "生产物流",
        "rects": [
          {
            "x": 565,
            "y": 210,
            "width": 405,
            "height": 635
          }
        ]
      },
      {
        "id": "QL-22-L03",
        "name": "销售物流",
        "rects": [
          {
            "x": 965,
            "y": 210,
            "width": 405,
            "height": 635
          }
        ]
      },
      {
        "id": "QL-22-L04",
        "name": "回收物流",
        "rects": [
          {
            "x": 1365,
            "y": 210,
            "width": 400,
            "height": 635
          }
        ]
      },
      {
        "id": "QL-22-L05",
        "name": "判断方法",
        "rects": [
          {
            "x": 165,
            "y": 850,
            "width": 1600,
            "height": 100
          }
        ]
      }
    ],
    "combinedRects": [
      {
        "x": 165,
        "y": 210,
        "width": 1600,
        "height": 740
      }
    ],
    "combinedFeathers": [
      10
    ]
  },
  {
    "page": "QL-23",
    "source": "ql-batch/QL-23.png",
    "layers": [
      {
        "id": "QL-23-L01",
        "name": "供应物流分工文字",
        "rects": [
          {
            "x": 165,
            "y": 255,
            "width": 380,
            "height": 125
          }
        ]
      },
      {
        "id": "QL-23-L02",
        "name": "生产物流分工文字",
        "rects": [
          {
            "x": 570,
            "y": 255,
            "width": 380,
            "height": 125
          }
        ]
      },
      {
        "id": "QL-23-L03",
        "name": "销售物流分工文字",
        "rects": [
          {
            "x": 975,
            "y": 255,
            "width": 380,
            "height": 125
          }
        ]
      },
      {
        "id": "QL-23-L04",
        "name": "回收物流分工文字",
        "rects": [
          {
            "x": 1375,
            "y": 255,
            "width": 385,
            "height": 125
          }
        ]
      },
      {
        "id": "QL-23-L05",
        "name": "数字场域场景",
        "rects": [
          {
            "x": 145,
            "y": 390,
            "width": 1630,
            "height": 420
          }
        ]
      },
      {
        "id": "QL-23-L06",
        "name": "升级结论",
        "rects": [
          {
            "x": 170,
            "y": 820,
            "width": 1580,
            "height": 110
          }
        ]
      }
    ],
    "combinedRects": [
      {
        "x": 145,
        "y": 250,
        "width": 1630,
        "height": 680
      }
    ],
    "combinedFeathers": [
      10
    ]
  }
] as const satisfies readonly PageConfig[];
