import requests
# import re
from lxml import etree

html_text = """
/Users/simupper/anaconda3/bin/python /Users/simupper/Documents/KRT/api/app/spider/student_certification.py






<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <title>教育部学历证书电子注册备案表_中国高等教育学生信息网（学信网）</title>
  <meta name="keywords" content="学历在线验证报告,教育部学历证书电子注册备案表,教育部学籍在线验证报告,学历查询,学历验证,学信网" />
  <meta name="description" content="" />
  <link href='https://t3.chei.com.cn/chsi/css/common2014.css?20180828' rel="stylesheet" type="text/css" />
  <link href='https://t1.chei.com.cn/common/css/share.css' rel="stylesheet" type="text/css" />
  <meta content="{qqqqr0qqr0r4qqr0XHywUg0BLstWiTl4ipeNX4U6lcWfynqIH8ZQx_2kOrRlh2Aqqr7D0c184fqqr0QFTNQF2xXKKyRRm2zKbyIVmy1UYmwqqVVt2fvCKI3yJOvbbFFxNG)ksSlVFb0.o03Zx6f6x0AiVnL7tUJ_8rqzDUZEH6YmEKLOsDJHi9gOknmpE02O1kNhEaAfUcJD30V_AcJa3aaJIc0xrUGxpf2bxA3FkcVqw6pykPTgMAqVYsNAESlf1nJs3ng_h1JXEs3OtDW.iPLOFnleEnV1Rb0HH6A_J1x5rvgvqSQfx1q_FGqUopEiwoVWE10OJKW0iOQOQclLEuxOWsLWE00fmnWH3aL_c1W430VtDGa_qaQRU13Xca7RhqE480YdxqVsMV9VDOLRETLfqPWV3SQ_mPJUEA9OlKWAifWO.co0E5g1.C6WhiEgykO8xQyy4ck1JZmC6pvEtJ7E.UUhE8AOdbHeiBGOX1oOEdzOeO.TE43f4PHa3dW_ZPHc3gEq9odDcQETgP6tmwxeyk6aD8A341hFMR3Vau.cEgWfS1Hw3ea_6ni3EQqOCbHRizAO21oHEeQ19D6L8Wy_CA1_8jRyjcPt8_Gv.P1Or.li_vK1EMZONCiPijlOgPD_E4SOBuj5EdZfL1iy34G_Xnim3d7Ajn_cEh7I.rFvD89t2cC2JLWzfpcmMwZVPkjhEZAfvciD3gV_GcHrER7OGCi8iN0O6PDDEyG1CKCIr43R7aisoWZznUn3ELGcPcCxHOVfECNRHv3ZFoS.xKLZtuyeHDYZRcYvHcq58kSPIDl2IkSWIkqeRS29qKAUwqxM39Z2IbRNRbNNU1NQQPAhQ1YWHq05YuSHIlL21satH2EZpoSoxV3ZruyRHllJqvxFo9E8wuptxmxPprNQcmZrqcVEmTEpDDNGH99ZVUSAxYWZMkg0HcyZh1VLHD95Wua.Ic32xsaUID92ik9hqnxGEr2bWfZeRG9RrrEQmuAvQb0hJPVTHo35hOaaIkW2WOSuHfVZkUaWxAZZ1kgAHqLJDvaDxAVZJTLqq..hfro45p5HBaV6KggRtI1ftMj2kqEX4muvUNhBDw1zq~R3D7AxGaCqAaatY7LY1lEcAVVqVGlo1g7xS7nEY70J1ZCkpJkVlQolpLehaV6XmXuK80DzabSW.gEuAU8JWZW_mB.cXEOTq.7W.V0gmkjVBQUymBaEeGkaaouYjSY_a.qhFWuZTBXcHEt0phFqQLkanuvxeVbvn8AmilRuPsXk5rpgOM3rzfMnGdHiIQsn1UbkWLlPc45Y5lXaAH_tIaLTYBqD70OeGBStILmffU4Dxqr2YFbEFWYjkjIsBQk5YOerjziLpH6xtlzfp1jqyA7zScesXWkyYOfr.wiBpHOKMLn7mUOWyLb7uovKgyU2cbLkLlDjrczDzgXfuFuxjaC61iXiRWqqqqqqh8lHgcd2do0xqqqY32sUCEMwB.Gg3DxAzFdJwc64qqh6Hk0WZg0Svdc64qqr0l1ur9q!m7z,aac,amr,asm,avi,bak,bat,bmp,bin,c,cab,css,csv,com,cpp,dat,dll,doc,dot,docx,exe,eot,fla,flc,fon,fot,font,gdb,gif,gz,gho,hlp,hpp,htc,ico,ini,inf,ins,iso,js,jar,jpg,jpeg,json,java,lib,log,mid,mp4,mpa,m4a,mp3,mpg,mkv,mod,mov,mim,mpp,msi,mpeg,obj,ocx,ogg,olb,ole,otf,py,pyc,pas,pgm,ppm,pps,ppt,pdf,pptx,png,pic,pli,psd,qif,qtx,ra,rm,ram,rmvb,reg,res,rtf,rar,so,sbl,sfx,swa,swf,svg,sys,tar,taz,tif,tiff,torrent,ttf,vsd,vss,vsw,vxd,woff,woff2,wmv,wma,wav,wps,xbm,xpm,xls,xlsx,xsl,xml,z,zip,apk,plist,ipak162W8CfkU0JMATxWqqt10831790481YbeymuLsh2g0mUGUiAqql4096qqqh5m.oKt68HOfGrIJu9DjA3WflL08asjqCzuUtA7SJu085"><!--[if lt IE 9]><script r='m'>document.createElement("section")</script><![endif]--><script type="text/javascript" charset="utf-8" src="/NJ7TNwcMIDHl/DlMKtecDLfpo.0c184fa.js" r='m'></script><script type="text/javascript" r='m'>(function(){var _$gD=16,_$$I=[[12,11,5,8,5,12,3,0,10,0,6,8,9,12,3,2,5],[14,70,104,15,71,82,66,91,77,91,98,15,57,88,79,48,102,48,2,93,67,0,53,116,96,27,76,121,91,117,36,22,28,110,20,25,21,11,110,13,29,52,29,39,31,49,96,8,12,85,15,1,110,42,79,10,17,5,100,106,16,109,16,47,110,69,91,83,39,84,103,68,43,91,40,110,91,46,53,15,80,61,9,88,94,80,84,115,35,56,74,124,108,106,70,19,64,24,120,60,26,93,92,62,82,109,44,30,4,48,28,34,81,54,91,110,54,79,112,107,107,17,5,65,4,93,97,121,114,54,119,106,72,86,36,39,102,68,86,14,61,60,21,118,40,70,81,49,115,114,29,103,64,106,2,95,20,27,86,61,37,60,91,33,40,101,32,34,6,74,104,40,87,85,120,96,62,59,22,48,100],[0,25,7,15,2,0,14,19,1,26,12,3,5,14,10,22,20,28,8,33,32,25,35,31,24,16,24,15,22,27,21,24,21,17,24,23,24,22,30,3,9,22],[47,3,24,7,27,56,33,49,29,41,29,19,39,39,37,4,6,37,20,40,30,28,38,28,43,16,27,0,21,32,12,48,32,50,3,25,17,4,19,25,12,45,12,2,18,8,14,44,43,11,14,44,20,29,1,34,13,31,8,27,44,13,24,0,10,46,5,42,33],[26,9,21,22,0,7,6,14,41,9,4,18,42,10,6,31,42,25,1,16,15,28,37,38,39,11,5,40,40,32,29,43,36,24,17,18,13,41,29,23,20,36,2,24,10,47,35,32,7,28,9,30,14,8,9]];function _$vd(_$8T){var _$$Z=_$8T.length;var _$3D,_$b5=new _$TT(_$$Z-1),_$OU=_$8T.charCodeAt(0)-97;for(var _$a7=0,_$4O=1;_$4O<_$$Z; ++_$4O){_$3D=_$8T.charCodeAt(_$4O);if(_$3D>=40&&_$3D<92){_$3D+=_$OU;if(_$3D>=92)_$3D=_$3D-52;}else if(_$3D>=97&&_$3D<127){_$3D+=_$OU;if(_$3D>=127)_$3D=_$3D-30;}_$b5[_$a7++ ]=_$3D;}return _$cq.apply(null,_$b5);}function _$4O(_$8T){var _$$Z=_$cq(96);var _$3D=_$vd(_$8T).split(_$$Z);for(var _$b5=0;_$b5<_$3D.length;_$b5++ ){_$1l.push(Number(_$3D[_$b5]));}}function _$a7(_$8T,_$cJ){return _$7q[_$Y_[39]].abs(_$8T)%_$cJ;}function _$b5(_$8T){var _$$Z=_$cq(96);_$Y_=_$vd(_$8T).split(_$$Z);}function _$7X(_$OU){var _$CM=_$OU[_$a7(_$bV(),16)];var _$wa=_$cy(_$OU);_$OU[7]=_$nU();var _$wa=_$fG();return _$OU[_$a7(_$2d()-_$OU[_$a7(_$0B(),16)],16)];}function _$bV(){return 4}function _$cy(_$OU){_$OU[_$a7(_$fG(),16)]=_$KJ();_$KA(_$OU);_$JI(_$OU);_$v3(_$OU);return _$o4();}function _$fG(){return 9}function _$KJ(){return 15}function _$KA(_$OU){var _$9J=_$Qf();var _$CM=_$bV();_$OU[_$a7(_$I_(),16)]=_$fG();var _$CM=_$2d();_$OU[_$a7(_$0B(),16)]=_$Qf();return _$bV();}function _$Qf(){return 6}function _$I_(){return 3}function _$2d(){return 5}function _$0B(){return 8}function _$JI(_$OU){var _$wa=_$KJ();var _$9J=_$2d();var _$9J=_$o4();_$OU[7]=_$nU();return _$I_();}function _$o4(){return 1}function _$nU(){return 13}function _$v3(_$OU){_$OU[15]=_$2d();var _$CM=_$Qf();var _$CM=_$bV();_$OU[_$a7(_$I_(),16)]=_$fG();var _$CM=_$2d();return _$x5();}function _$x5(){return 11}var _$Y_,_$1l,_$73,_$0W,_$7q,_$cq,_$TT,_$7X,_$i5,_$N_,_$7m,_$7_;var _$WY,_$3D,_$aw=_$gD,_$84=_$$I[0];while(1){_$3D=_$84[_$aw++];if(50<43+_$3D&&_$3D<12){if(118===_$3D+110){if( !_$WY)_$aw+=1;}else if(_$3D===9){_$7q=window,_$0W=String,_$TT=Array,_$i5=document,_$7m=Date;}else if(65-_$3D<56&&-41>_$3D-52){_$TT=Array;}else{_$b5('ptgp{`cp}s~|`n`.`$_ed`UrV)Yup`dfqdec`Q`Nl`nt{dt xuM`2rexgtI@qytre`dhxerwM`ctda~}dtEtie`~}ctpsjdepetrwp}vt`u{~~c`Spaa{jMewxdQ`rp{{`da{xe`],2ccpjSac~e~ejatSafdwSpaa{jM`~at}`,`MNlgpc `drcxaed`qctpz,`I>=9eeaCtbftde`Muf}rex~}MNlgpc `.$_edSptqx,`uf}rex~} `L\\c\\}\\d]`uf}rex~}tgp{MNlL}pexgtr~st]n`+`ptqx`hwx{tMVNl`v`dt}s`titrDrcxae`L`rwpc4~st2e`ctpsjDepet`>pew`NMN,`PP],`>xrc~d~ueSI>=9EEA`xuM`M`.$_edSdryQ`rpdt `f}dwxue`uc~|4wpc4~st`vteEx|t`cta{prt`e~Decx}v`nt{dtl`Qpcvf|t}edN,ctefc} `gpc `-');}}else if(_$3D>3&&-56<-7*_$3D){if(116===_$3D+112){_$aw+=5;}else if(_$3D===5){_$M4(174);_$aw=0;}else if(57-_$3D<52&&-60>_$3D-67){_$4O('wOTQVR`ONPR`R`RNWT`NLS`Nbnnnn`PST`OT`TSSQT`TR`U`ONN`P');}else{_$N_=_$7q[_$Y_[4]];}}else if(4>_$3D){if(41===_$3D+41){_$WY= !_$N_;}else if(_$3D===1){_$aw+=-5;}else if(103-_$3D<102&&-72>_$3D-75){_$7_=[_$1l[2],_$1l[7],_$1l[9],_$1l[6],_$1l[1],_$1l[3],_$1l[0],_$1l[8]];}else{return;}}else{if(56===_$3D+42){_$N_=_$7q[_$Y_[4]]={};}else if(_$3D===13){_$Y_=[],_$1l=[],_$cq=String.fromCharCode;}else{_$M4(0);}}}function _$M4(_$9J,_$8T){function _$Pe(){return _$E_[_$Y_[37]](_$yh++ );}var _$3D,_$84,_$OU,_$Oo,_$$Z,_$TN,_$o5,_$9L,_$yh,_$E_,_$QR,_$y5,_$a7,_$b5,_$4O,_$gD,_$aw,_$WY,_$5d;var _$CM,_$cy,_$wa=_$9J,_$fG=_$$I[1];while(1){_$cy=_$fG[_$wa++];if(191>127+_$cy){if(38>22+_$cy){if(61>57+_$cy){if(3===_$cy){_$$Z+="mM4mgIrFja7b54OgDawWY5d3D84OUOo$Z9JwaCMbVcyfGKJKAQfI_2d0BJIo4nUv3x5lpRf9dX4LBLjnPuIZpnXTUJq5x41Bh9r1zT8lJC";}else if(27===_$cy+26){var _$yh=0;}else if(_$cy===2){return 13;}else{_$QR=_$E_[_$Y_[6]](_$yh,_$aw)[_$Y_[17]](_$0W[_$Y_[48]](1));}}else if(66<63+_$cy&&_$cy<8){if(7===_$cy){for(_$$Z=0,_$3D=0;_$3D<_$b5;_$3D+=_$1l[12]){_$OU[_$$Z++ ]=_$a7+_$8T[_$Y_[6]](_$3D,_$1l[12]);}}else if(28===_$cy+23){_$8T._$T0="_$cT";}else if(_$cy===6){return 15;}else{for(_$WY=0;_$WY<_$gD;_$WY++ ){_$84.push(_$Y_[2]);}}}else if(_$cy>7&&-900<-75*_$cy){if(11===_$cy){var _$gD=_$Pe();}else if(111===_$cy+102){_$gD=_$Pe();}else if(_$cy===10){_$$Z+="0aQsl1ktxEuCLu1WvkyMEzisj9S7jo16NYQ8mCE5TOvA6DNiWjUSLRZ$jGsPG5piYpoRhpAjiUXr42ZIVyxplqMhvSgV1xCSjAmmY0iC0U9gjX7l";}else{_$3D=_$7q[_$Y_[0]];}}else{if(15===_$cy){_$N_._$Qf=_$M4(14);}else if(47===_$cy+34){var _$aw=_$Pe()*_$1l[5]+_$Pe();}else if(_$cy===14){if( !_$CM)_$wa+=2;}else{var _$OU=_$Pe();}}}else if(20<5+_$cy&&_$cy<32){if(15<_$cy&&134>114+_$cy){if(19===_$cy){_$8T._$aQ="_$iG";}else if(88===_$cy+71){_$N_._$mI=_$M4(8)-_$$Z;}else if(_$cy===18){_$8T._$Bh="_$H7";}else{for(_$WY=0;_$WY<_$gD;_$WY++ ){_$mg(16,_$WY,_$84);}}}else if(88<69+_$cy&&_$cy<24){if(23===_$cy){_$N_[_$Y_[5]]=_$73;}else if(81===_$cy+60){var _$TN=_$N_[_$Y_[31]]=[];}else if(_$cy===22){_$8T._$bt="_$jT";}else{var _$b5=_$E_.length;}}else if(_$cy>23&&-224<-8*_$cy){if(27===_$cy){_$8T._$lT="iuqq48_vexq";}else if(89===_$cy+64){_$8T._$Kv="_$6t";}else if(_$cy===26){_$$Z+="3TKYtMQspL9yjBTucd1IQAk03igKSVsWZkjfp00obgI_Fz77l_dcUr6WpE1TWArDB65RVvjAfpbSVI5uY$kBUNcAtMKSK3G$o1JAoeEqaWkbU3C3";}else{var _$3D=_$M4(67);}}else{if(31===_$cy){var _$Oo=_$M4(8);}else if(115===_$cy+86){var _$o5=_$N_._$Qf;}else if(_$cy===30){var _$9L=_$Pe();}else{_$wa+=-25;}}}else if(_$cy>31&&-4656<-97*_$cy){if(31<_$cy&&138>102+_$cy){if(35===_$cy){_$8T._$dx="_$0B";}else if(153===_$cy+120){return 2;}else if(_$cy===34){_$8T._$cJ=4;}else{_$yh+=_$aw;}}else if(139<104+_$cy&&_$cy<40){if(39===_$cy){return _$M4(144)+_$M4(154);}else if(101===_$cy+64){return 5;}else if(_$cy===38){_$$Z=_$$Z[_$Y_[50]](RegExp(_$Y_[28],_$Y_[33]),"");}else{_$M4(115,_$8T);}}else if(_$cy>39&&-660<-15*_$cy){if(43===_$cy){var _$E_=_$N_[_$Y_[5]];}else if(169===_$cy+128){_$CM=_$8T===undefined||_$8T==="";}else if(_$cy===42){return 0;}else{return 4;}}else{if(47===_$cy){var _$y5=_$Pe();}else if(86===_$cy+41){_$8T._$sl="_$1Z";}else if(_$cy===46){_$M4(74,_$5d);}else{var _$$Z;}}}else{if(47<_$cy&&170>118+_$cy){if(51===_$cy){var _$4O=_$Pe();}else if(110===_$cy+61){_$wa+=25;}else if(_$cy===50){_$8T._$$I="_$S9";}else{return 11;}}else if(102<51+_$cy&&_$cy<56){if(55===_$cy){_$8T._$6I="_$Wm";}else if(174===_$cy+121){_$$Z+="iJY_1l730W7qvdcqTT7Xi5N_7m7_8TcJPeNfTNo59LyhE_QRy5Hv951G$edx8s_RNNEaJhF02xWgJpeeOVik$xKEUcFpAyCbTuXM66$In";}else if(_$cy===54){_$8T[_$M4(143,_$M4(160))]=_$M4(169);}else{_$$Z+="06OFqqL9_sRAJEodyDs6kCFRwFaRbft7bEEwfs1Wcx3XYPRTIDkPTGK1KZyAq68abH23s7JE$4W9sIZfMzr_KKaAQEmN9TjkAjGO3Nx8VKwPLnTd4x";}}else if(_$cy>55&&-7440<-124*_$cy){if(59===_$cy){for(_$OU=0;_$OU<_$$I.length;_$OU++){_$84=_$$I[_$OU];for(_$Oo=0;_$Oo<_$84.length;_$Oo++){_$84[_$Oo]^=_$3D[Math.abs(_$Oo)%16];}}return;}else if(125===_$cy+68){_$8T._$WY="_$lJ";}else if(_$cy===58){_$CM=_$7q[_$Y_[35]];}else{return _$OU;}}else{if(63===_$cy){_$8T._$P3=_$7X;}else if(136===_$cy+75){_$8T._$HN="sXbAL3Cca7A";}else if(_$cy===62){_$M4(131,_$3D);}else{_$wa+=2;}}}}else{if(63<_$cy&&157>77+_$cy){if(63<_$cy&&192>124+_$cy){if(67===_$cy){_$mg(0);}else if(99===_$cy+34){_$8T._$x7="_$L$";}else if(_$cy===66){_$$Z+="BoO2rdlPOe1mzh_wqwHDx1hl5NGvIx4oJjTowXAc50rr7mJXgbtSlCjb6eUlW58GlLpHKK4Jl0GWbsMcWH7OdH6RlS9uJP3six7sU6tnZL$X2T";}else{var _$$Z='';}}else if(93<26+_$cy&&_$cy<72){if(71===_$cy){_$M4(86,_$N_);}else if(81===_$cy+12){return 1;}else if(_$cy===70){_$M4(29);}else{_$N_._$sU=_$M4(8)-_$$Z;}}else if(_$cy>71&&-4256<-56*_$cy){if(75===_$cy){_$8T._$zX="_$wH";}else if(120===_$cy+47){_$8T._$Sl="_$vI";}else if(_$cy===74){return 10;}else{if(_$M4(160)){_$8T[_$M4(143,_$M4(179))]=_$M4(148);}}}else{if(79===_$cy){_$8T[_$M4(143,_$M4(148))]=_$M4(180);}else if(169===_$cy+92){_$$Z+="jlC6$wcrJGAHP1oQVdrEzcjwz9VxJcdzN8Lpy";}else if(_$cy===78){var _$84=[];}else{return new _$7m()[_$Y_[49]]();}}}else if(171<92+_$cy&&_$cy<96){if(79<_$cy&&129>45+_$cy){if(83===_$cy){_$8T._$Dx="f79lUpP4DEYHW9LNe1b94a";}else if(168===_$cy+87){_$$Z=_$7q[_$Y_[35]](_$8T);}else if(_$cy===82){var _$$Z=_$7q[_$Y_[0]][_$Y_[51]]();}else{_$8T._$1k="_$_A";}}else if(119<36+_$cy&&_$cy<88){if(87===_$cy){_$8T._$NG="MkVDWW9R2xenhu.3LI2gWA";}else if(97===_$cy+12){_$8T._$oJ=51;}else if(_$cy===86){_$8T[_$M4(143,_$M4(154))]=_$M4(163);}else{_$CM=_$gD>0;}}else if(_$cy>87&&-2852<-31*_$cy){if(91===_$cy){return 6;}else if(139===_$cy+50){_$$Z=_$3D[_$Y_[16]](_$7q,_$8T);}else if(_$cy===90){return;}else{_$wa+=1;}}else{if(95===_$cy){return _$$Z;}else if(177===_$cy+84){_$8T._$wq="EP_PbZ9q6Pa";}else if(_$cy===94){_$CM=_$$Z!==_$Y_[29];}else{_$$Z+="ea4D_uDHNe5shJ2YmAL7z8eiR96EGZ3E3iXFbaVQEwPxFrw6I7nHQlTOJzXZxU_ymDC5_WzKvoW87PS2YxVBAiOWmLydFtn29mI6CHcR04GC";}}}else if(_$cy>95&&-9632<-86*_$cy){if(95<_$cy&&141>41+_$cy){if(99===_$cy){var _$$Z,_$3D,_$b5=_$8T.length,_$OU=new _$TT(_$b5/_$1l[12]),_$a7='_$';}else if(106===_$cy+9){_$$Z+="ToPYET3FyvqKVl7WMgaE$dL8qnnMeFkxurAxcubLrNQH0fu4f19II90PLRsqsJ7KWoXoAaGHlkosqh5DjQKkcnry_C07zSmGzcGtG8XvO$Av1U_2i";}else if(_$cy===98){var _$5d=_$84.join('');}else{for(_$OU=0;_$OU<16;_$OU++)_$3D[_$OU]=1;}}else if(109<10+_$cy&&_$cy<104){if(103===_$cy){var _$a7=_$Pe();}else if(172===_$cy+71){_$84.push(_$Y_[40]);}else if(_$cy===102){if( !_$CM)_$wa+=1;}else{return 1;}}else if(_$cy>103&&-8532<-79*_$cy){if(107===_$cy){return 7;}else if(228===_$cy+123){_$CM=_$N_[_$Y_[5]];}else if(_$cy===106){_$8T[14]=_$M4(168);}else{_$8T._$0G="_$sM";}}else{if(111===_$cy){}else if(166===_$cy+57){_$8T._$K4="_$b6";}else if(_$cy===110){_$8T[14]=_$M4(168);}else{_$8T._$Lj=247;}}}else{if(115<_$cy&&154>34+_$cy){if(119===_$cy){var _$$Z=_$M4(8);}else if(215===_$cy+98){_$$Z+="h$OW4z_fU2XYgYfDV3XKm9y4Uih1R2FyNLGp9GMjERDdfX6vGYCw_d50u6mcp2RdJXDTDUxmEelkS_67OMMpYOLLV$9hdliOQWSED3IF6LS0pCRkUrK";}else if(_$cy===118){return Math.abs(arguments[1]) % 16;}else{_$8T._$uJ="_$cW";}}else if(212<101+_$cy&&_$cy<116){if(115===_$cy){return 8;}else if(177===_$cy+64){return _$M4(10,_$$Z);}else if(_$cy===114){_$8T._$o5=187;}else{return _$M4(162);}}else{if(121===_$cy){_$8T._$Lp="_$7q";}else{_$3D=[];}}}}}function _$mg(_$gD,_$Hv,_$95){function _$1G(){var _$5d=[0];Array.prototype.push.apply(_$5d,arguments);return _$Ir.apply(this,_$5d);}var _$NN,_$Ea,_$Jh,_$F0,_$2x,_$Wg,_$Jp,_$ee,_$OV,_$ik,_$a7,_$b5,_$4O,_$dx,_$8s,_$_R;var _$WY,_$3D,_$aw=_$gD,_$84=_$$I[2];while(1){_$3D=_$84[_$aw++];if(15<_$3D&&79>47+_$3D){if(15<_$3D&&79>59+_$3D){if(19===_$3D){var _$Wg=_$Pe();}else if(90===_$3D+73){var _$8s=_$mg(11);}else if(_$3D===18){_$Jh[_$Y_[34]]();}else{_$TN[_$Hv]=_$b5;}}else if(97<78+_$3D&&_$3D<24){if(23===_$3D){return;}else if(94===_$3D+73){var _$Jh=_$Pe();}else if(_$3D===22){var _$OV=_$mg(11);}else{var _$b5=_$mg(11);}}else if(_$3D>23&&-3024<-108*_$3D){if(27===_$3D){var _$F0=_$mg(11);}else if(62===_$3D+37){}else if(_$3D===26){var _$2x=_$mg(11);}else{var _$4O=_$b5>1?_$i5[_$Y_[22]][_$b5-_$1l[12]].src:_$73;}}else{if(31===_$3D){var _$dx=[];}else if(142===_$3D+113){var _$ee=_$Pe();}else if(_$3D===30){var _$Ea=_$Pe();}else{var _$4O=_$Pe();}}}else if(_$3D<16){if(65>61+_$3D){if(3===_$3D){_$Jh=_$7q[_$Y_[10]]?new _$7q[_$Y_[10]](_$Y_[42]):new _$7q[_$Y_[24]]();}else if(23===_$3D+22){var _$b5=_$i5[_$Y_[22]].length;}else if(_$3D===2){for(_$a7=0;_$a7<_$4O;_$a7++ ){_$dx[_$a7]=_$mg(11);}}else{_$aw+=19;}}else if(43<40+_$3D&&_$3D<8){if(7===_$3D){_$aw+=-19;}else if(130===_$3D+125){return _$4O;}else if(_$3D===6){_$WY=_$4O;}else{var _$4O=new _$TT(_$b5);}}else if(_$3D>7&&-1476<-123*_$3D){if(11===_$3D){var _$b5=_$Pe();}else if(14===_$3D+5){var _$Jp=_$Pe();}else if(_$3D===10){_$Jh[_$Y_[19]]('GET',_$4O,false);}else{_$Ir(7,_$95);}}else{if(15===_$3D){_$Jh[_$Y_[13]]=_$1G;}else if(100===_$3D+87){_$aw+=18;}else if(_$3D===14){if( !_$WY)_$aw+=4;}else{for(_$a7=0;_$a7<_$b5;_$a7++ ){_$4O[_$a7]=_$Pe();}}}}else{if(32===_$3D){var _$_R=_$Pe();}else if(101===_$3D+68){var _$ik=_$Pe();}else{var _$NN=_$Pe();}}}function _$Ir(_$4O,_$$x){var _$a7,_$b5,_$Uc,_$Fp;var _$aw,_$5d,_$gD=_$4O,_$3D=_$$I[3];while(1){_$5d=_$3D[_$gD++];if(-672<-42*_$5d){if(-300<-75*_$5d){if(_$5d===1){_$$x.push(_$o5[_$Jh]);}else if(-98>_$5d-99){_$$x.push(_$Hv);}else if(2===_$5d){if( !_$aw)_$gD+=4;}else{for(_$a7=0;_$a7<_$2x.length;_$a7+=_$1l[12]){if(_$1l[4]<Math[_$Y_[1]]()){_$b5.push([_$2x[_$a7],_$2x[_$a7+1]]);}else{_$b5[_$Y_[47]]([_$2x[_$a7],_$2x[_$a7+1]]);}}}}else if(-345>-115*_$5d&&8>_$5d){if(_$5d===5){_$$x.push("=0,");}else if(128-_$5d<125&&-11>_$5d-16){_$Fj(10,0,_$dx.length);}else if(6===_$5d){_$aw=_$N_[_$Y_[5]];}else{_$$x.push(_$o5[_$y5]);}}else if(7<_$5d&&44>32+_$5d){if(_$5d===9){_$$x.push(_$Y_[32]);}else if(51-_$5d<44&&-117>_$5d-126){for(_$a7=0;_$a7<_$8s.length;_$a7++ ){_$$x.push(_$Y_[7]);_$$x.push(_$o5[_$8s[_$a7]]);}}else if(10===_$5d){_$$x.push(_$Y_[7]);}else{_$$x.push(_$Y_[41]);}}else{if(_$5d===13){_$gD+=-32;}else if(118-_$5d<107&&-27>_$5d-40){_$aw=_$dx.length;}else if(14===_$5d){for(_$a7=1;_$a7<_$F0.length;_$a7++ ){_$$x.push(_$Y_[7]);_$$x.push(_$o5[_$F0[_$a7]]);}}else{_$$x.push(_$o5[_$Ea]);}}}else if(-1695>-113*_$5d&&32>_$5d){if(_$5d>15&&-1080<-54*_$5d){if(_$5d===17){_$aw=_$8s.length;}else if(122-_$5d<107&&-53>_$5d-70){_$$x.push(_$o5[_$F0[0]]);}else if(18===_$5d){_$$x.push(_$Y_[20]);}else{_$$x.push(_$o5[_$NN]);}}else if(-2052>-108*_$5d&&24>_$5d){if(_$5d===21){_$$x.push(_$o5[_$9L]);}else if(45-_$5d<26&&-59>_$5d-80){_$$x.push(_$Y_[8]);}else if(22===_$5d){_$$x.push(_$Y_[27]);}else{_$$x.push(_$Y_[36]);}}else if(23<_$5d&&63>35+_$5d){if(_$5d===25){_$M4(74,_$Jh[_$Y_[12]]);}else if(11-_$5d<-12&&-47>_$5d-72){_$$x.push(_$Y_[54]);}else if(26===_$5d){if( !_$aw)_$gD+=1;}else{_$aw=_$Hv==0;}}else{if(_$5d===29){_$$x.push(_$Y_[44]);}else if(64-_$5d<37&&28>_$5d-1){_$gD+=32;}else if(30===_$5d){if( !_$aw)_$gD+=10;}else{_$gD+=8;}}}else if(31<_$5d&&176>128+_$5d){if(_$5d>31&&-2808<-78*_$5d){if(_$5d===33){_$Fj(47);}else if(79-_$5d<48&&-83>_$5d-116){return;}else if(34===_$5d){var _$b5=[];}else{_$$x.push("];");}}else if(-3535>-101*_$5d&&40>_$5d){if(_$5d===37){_$$x.push(_$Y_[25]);}else if(80-_$5d<45&&-2>_$5d-39){_$$x.push(_$Y_[45]);}else if(38===_$5d){if( !_$aw)_$gD+=8;}else{_$$x.push(_$o5[_$ik]);}}else if(39<_$5d&&70>26+_$5d){if(_$5d===41){_$$x.push(_$Y_[26]);}else if(16-_$5d<-23&&-2>_$5d-43){_$$x.push(_$o5[_$Jp]);}else if(42===_$5d){_$$x.push(_$o5[_$ee]);}else{_$$x.push(_$Y_[2]);}}else{if(_$5d===45){_$$x.push(_$Y_[3]);}else if(86-_$5d<43&&11>_$5d-34){var _$Uc=0;}else if(46===_$5d){_$aw=_$Jh[_$Y_[38]]==_$1l[2];}else{_$Uc=_$dx.length;}}}else{if(_$5d===49){for(_$a7=0;_$a7<_$b5.length;_$a7++ ){_$Fj(0,_$b5[_$a7][0],_$b5[_$a7][1],_$$x);}}else if(24-_$5d<-23&&3>_$5d-46){var _$a7,_$Fp=_$1l[2];}else if(50===_$5d){_$M4(29);}else{_$aw=_$F0.length;}}}function _$Fj(_$Oo,_$Ay,_$Cb,_$Tu){var _$3D,_$84,_$OU,_$a7,_$b5,_$4O,_$gD,_$aw,_$WY,_$5d;var _$9J,_$CM,_$$Z=_$Oo,_$bV=_$$I[4];while(1){_$CM=_$bV[_$$Z++];if(16>_$CM){if(-560>-80*_$CM&&12>_$CM){if(16-_$CM<7&&-54>_$CM-65){_$3D=_$5d%_$4O;}else if(9===_$CM){_$$Z+=29;}else if(41===_$CM+33){return;}else{_$$Z+=5;}}else if(3<_$CM&&127>119+_$CM){if(79-_$CM<74&&-68>_$CM-75){_$3D-=_$3D%_$1l[12];}else if(5===_$CM){var _$3D,_$b5,_$OU,_$4O=_$Cb-_$Ay;}else if(56===_$CM+52){_$WY=_$a7[0];}else{_$9J=_$3D.length!=_$b5;}}else if(_$CM<4){if(44-_$CM<43&&-26>_$CM-29){_$$x.push(_$QR[_$OV[_$3D]]);}else if(1===_$CM){_$b5-=_$b5%_$1l[12];}else if(2===_$CM+2){_$$Z+=25;}else{_$Fj(10,_$Ay,_$Cb);}}else{if(31-_$CM<18&&-2>_$CM-17){if( !_$9J)_$$Z+=15;}else if(13===_$CM){for(_$OU=0;_$OU<_$b5;_$OU+=_$1l[12]){_$$x.push(_$QR[_$3D[_$OU]]);_$$x.push(_$o5[_$3D[_$OU+1]]);}}else if(57===_$CM+45){_$OU=0;}else{if( !_$9J)_$$Z+=1;}}}else if(15<_$CM&&79>47+_$CM){if(-2645>-115*_$CM&&28>_$CM){if(101-_$CM<76&&-58>_$CM-85){_$9J=_$4O==0;}else if(25===_$CM){_$Fj(2,_$a7[_$3D]);}else if(38===_$CM+14){_$Fj(2,_$Ay);}else{_$Tu.push([_$Y_[27],_$o5[_$Ay],_$Y_[21],_$o5[_$_R],"=[",_$Cb,_$Y_[18],_$o5[_$_R],_$Y_[53],_$o5[_$Wg],_$Y_[15],_$o5[_$_R],");}"].join(''));}}else if(19<_$CM&&118>94+_$CM){if(57-_$CM<36&&-23>_$CM-46){_$b5=_$Y_[43];}else if(21===_$CM){for(;_$Ay+_$OU<_$Cb;_$Ay+=_$OU){_$$x.push(_$b5);_$$x.push(_$o5[_$NN]);_$$x.push(_$Y_[55]);_$$x.push(_$Ay+_$OU);_$$x.push(_$Y_[8]);_$Fj(10,_$Ay,_$Ay+_$OU);_$b5=_$Y_[9];}}else if(48===_$CM+28){var _$3D=_$dx[_$Ay];}else{var _$b5=_$3D.length;}}else if(118<103+_$CM&&_$CM<20){if(89-_$CM<72&&-3>_$CM-22){_$84=_$5d%_$Fp;}else if(17===_$CM){_$9J=_$4O<=_$Fp;}else if(46===_$CM+30){_$$x.push(_$Y_[2]);}else{_$$Z+=8;}}else{if(67-_$CM<38&&21>_$CM-10){_$9J=_$4O==1;}else if(29===_$CM){_$$Z+=-5;}else if(55===_$CM+27){}else{_$9J=_$OV.length!=_$3D;}}}else{if(-3510>-90*_$CM&&44>_$CM){if(85-_$CM<44&&-71>_$CM-114){for(_$3D=0;_$3D<_$4O-1;_$3D++ ){if(_$3D==_$84){_$aw=_$Cb;if(_$Ay>1&&_$5d%_$1l[12]==0){_$aw=_$Ay-1;}_$$x.push(_$b5);_$$x.push(_$o5[_$NN]);_$$x.push(_$gD);_$$x.push(_$aw);_$$x.push(_$Y_[8]);_$Fj(2,_$5d%_$Uc);_$b5=_$Y_[9];}_$$x.push(_$b5);_$$x.push(_$o5[_$NN]);_$$x.push(_$gD);_$$x.push(_$a7[_$3D]);_$$x.push(_$Y_[8]);_$Fj(2,_$a7[_$3D]);_$b5=_$Y_[9];}}else if(41===_$CM){_$a7[_$3D]=_$WY;}else if(98===_$CM+58){_$$x.push(_$QR[_$3D[_$b5]]);}else{if( !_$9J)_$$Z+=2;}}else if(35<_$CM&&95>55+_$CM){if(63-_$CM<26&&-16>_$CM-55){_$5d=Math[_$Y_[14]]((Math[_$Y_[1]]()*_$1l[11])+1);}else if(37===_$CM){_$$x.push(_$Y_[52]);}else if(101===_$CM+65){_$a7=[];}else{for(_$3D=0;_$3D<_$4O;_$3D++ ){_$a7[_$3D]=_$Ay+_$3D;}}}else if(128<97+_$CM&&_$CM<36){if(85-_$CM<52&&-84>_$CM-119){_$gD="===";}else if(33===_$CM){var _$3D=_$OV.length;}else if(155===_$CM+123){_$a7[0]=_$a7[_$3D];}else{for(_$3D=1;_$3D<_$1l[10];_$3D++ ){if(_$4O<=_$7_[_$3D]){_$OU=_$7_[_$3D-1];break;}}}}else{if(2-_$CM<-41&&39>_$CM-6){_$$Z+=4;}else{for(_$b5=0;_$b5<_$3D;_$b5+=_$1l[12]){_$$x.push(_$QR[_$OV[_$b5]]);_$$x.push(_$o5[_$OV[_$b5+1]]);}}}}}}}}}})()</script><script type="text/javascript" src='https://t1.chei.com.cn/common/jquery/1.5.1/jquery.min.js'></script>
  <script type="text/javascript" src='https://t1.chei.com.cn/common/js/snsshare-1.0.1.js'></script>
  <link href='https://t1.chei.com.cn/chsi/css/report/new-add-2018.css?20201030' rel="stylesheet" >





  <script>
    function gaTrackerOutboundLink(ele,eventCategory,eventAction,eventLabel){
      gtag('event', eventAction, {
        'event_category': eventCategory,
        'event_label': eventLabel
      });
      return true;
    }
  </script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=UA-100524-1"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-100524-1');
  </script>
</head>
<body>

<h1>教育部学历证书电子注册备案表</h1>



<script type="text/javascript" src='https://t4.chei.com.cn/chsi/js/zhuge-1.0.2.js'></script>
<img src='https://t1.chei.com.cn/common/wap/images/share_xxw.jpg' width='0' height='0' style='position: absolute;top:-100px;left: 0' />
<style type="text/css">
  .t_nav li { padding-right:21px;}
  .t_top_nav_l {min-height: 1px;}
</style>
<div class="t_top_nav">
  <div class="width1000 clearfix">
    <div class="t_top_nav_l">&nbsp;
    </div>
    <div class="t_top_nav_r"><a href="/" target="_parent">首页</a>　|　<a href="/en/" target="_parent">English</a></div>
    <div class="clearit"></div>
  </div>
</div>
<div class="t_header">
  <div class="width1000 clearfix">
    <div class="t_h_logo"><a href="/" target="_parent" class="home"></a>&nbsp;</div>
    <h2><a href="/" target="_parent" class="home"></a>教育部学历查询网站、教育部高校招生阳光工程指定网站、全国硕士研究生招生报名和调剂指定网站</h2>
  </div>
</div>
<div class="t_nav">
  <ul class="width1000">
    <li style="padding-left:2px;"><a href="/" target="_parent">首页</a></li>
    <li><a href="https://my.chsi.com.cn/" target="_blank">学籍查询</a></li>
    <li><a href="/xlcx/index.jsp" target="_parent">学历查询</a></li>
    <li><a href="/xlcx/bgcx.jsp">在线验证</a></li>
    <li><a href="/xlrz/index2.jsp" target="_parent">出国教育背景服务</a></li>
    <li><a href="https://my.chsi.com.cn/archive/index.jsp#txjd" target="_blank">图像校对</a></li>
    <li><a href="https://my.chsi.com.cn/" target="_blank">学信档案</a></li>
    <li><a href="https://gaokao.chsi.com.cn/" target="_blank" title="教育部阳光高考信息平台">高考</a></li>
    <li><a href="https://yz.chsi.com.cn/" target="_blank" title="中国研究生招生信息网">研招</a></li>
    <li><a href="https://www.gatzs.com.cn/" target="_blank">港澳台招生</a></li>
    <li><a href="https://www.gfbzb.gov.cn/" target="_blank">征兵</a></li>
    <li><a href="https://www.ncss.cn/" target='_blank' onmousedown="gaTrackerOutboundLink(this,'ncssindex', 'click', 'frommenu');zhugeFun.goNcss('frommenu','ncssindex')" >就业</a></li>
    <li><a href="https://xz.chsi.com.cn/" target="_blank">学职平台</a></li>
    <li style="padding-right: 0;"><a href="https://jp.chsi.com.cn/" target="_blank">日本频道</a></li>
  </ul>
</div>
<script>
  //输入框获取焦点和失去焦点效果
  function eventFocusAndBlur(id,text){
    document.getElementById(id).onfocus = function(){
      if(this.value=="" || this.value==text){
        this.value = "";
      }
      this.style.color = "#333333";
    }
    document.getElementById(id).onblur = function(){
      if(this.value=="" || this.value==text){
        this.value = text;
        this.style.color = "#999999";
      }
    }
  }
  function goo(curr,adv_id){
    curr.href = "https://axvert.chsi.com.cn/goo.action?aid=" + adv_id + "&evtype=referer_blank";
    return true;
  }
</script>
<div class="main clearfix">
  <div class="m_yah"><a href="/">首页</a> &gt; <a href="/xlcx/bgcx.jsp">学籍/学历在线验证报告</a> &gt; 教育部学历证书电子注册备案表</div>



  <div class="m_s_l" id="leftMenu">
    <ul class="m_s_l_ul">
      <li class="onread"><span class="icon_list">&nbsp;</span><a href="/xlcx/bgcx.jsp">在线验证</a></li>
      <li><span class="icon_list">&nbsp;</span><a href="/xlcx/bgys.jsp">验证报告简介</a></li>
      <li><span class="icon_list">&nbsp;</span><a href="/xlcx/fwcs.jsp">防伪措施</a></li>
      <li><span class="icon_list">&nbsp;</span><a href="/xlcx/yzzw.jsp">验证真伪</a></li>
      <li><span class="icon_list">&nbsp;</span><a href="/xlcx/tdhyt.jsp">特点和用途</a></li>
      <li><span class="icon_list">&nbsp;</span><a href="/xlcx/rhsq.jsp">如何申请</a></li>
      <li><span class="icon_list">&nbsp;</span><a href="/xlcx/rhsy.jsp">如何使用</a></li>
      <li><span class="icon_list">&nbsp;</span><a href="/xlcx/rhyq.jsp">延长验证有效期</a></li>
      <li><span class="icon_list">&nbsp;</span><a href="/xlcx/tbsm.jsp">特别声明</a></li>
    </ul>
    <div style="text-align:center;">
      <a href="/zhaopin/index.jsp" target="_blank">
        <img src='https://t1.chei.com.cn/chsi/images/2014/zhaopin.jpg?20170630' width="180" height="120" />
      </a>
    </div>
  </div>
  <div class="m_s_r" id="rightCnt">
    <div class="m_cnt_l">
      <div class="chooseLan">



        请选择报告语种：
        <a href="/xlcx/bg.do?vcode=AUBGKX3N00G7H3BC&lang=CN" class="current">中文</a>  <a href="#" id="openerHref">英文</a>
        <div id="noenreport" title="申请英文版">
          <span class="noenreportArrow"></span>
          <a href="#" class="newLayerClose" title="关闭"></a>
          该备案表尚无对应的翻译件(英文)，您可登录 <a href="https://my.chsi.com.cn/archive/index.jsp#zxyz" target="_blank" style="color:#06C;">学信档案</a>进行申请。
        </div>


      </div>








      <div class="printBG clearfix">
        <a class="iconClick iconPrint" id="bindGA_print" href="#" title="打印">&nbsp;</a>
        <a class="iconClick iconDownload" id="bindGA_download" href="#' >" title="下载">&nbsp;</a>
        <a class="iconClick iconEmail" id="showEmail" href="#" title="发送">&nbsp;</a>
        <a class="iconClick iconXxewm" id="openxxewm" href="#" title="学信二维码">&nbsp;</a>
        <div class="newLayer" id="bgdy" style="padding-bottom: 13px">
          <span class="newLayerArrow" style="right:126px;"></span>
          <a href="#" class="newLayerClose" title="关闭"></a>
          <div class="alignC">
            <img src='https://t2.chei.com.cn/chsi/images/2014/bgyb.png' alt="报告样本" width='80' /><br />
            <a  class="bindGA colorBlue"  id="go_bindGA_print" href="#" title="打印报告" >打印报告</a><br />
            <a  id="go_zycp_print" href="/report/xueli/survey.do?vcode=AUBGKX3N00G7H3BC" title="问卷调查" target="_blank" class="dcwjA">调查</a>
          </div>
        </div>
        <div class="newLayer" id="bgxz" style="padding-bottom: 13px">
          <span class="newLayerArrow" style="right:85px;"></span>
          <a href="#" class="newLayerClose" title="关闭"></a>
          <div class="alignC">
            <img src='https://t2.chei.com.cn/chsi/images/2014/bgyb.png' alt="报告样本" width='80' /><br />
            <a  class="bindGA colorBlue"  id="go_bindGA_download" href="/report/xueli/download.do?vcode=AUBGKX3N00G7H3BC&amp;rid=63432684787588944585916146095733&amp;ln=cn" title="打印报告" >下载报告</a><br />
            <a id="go_zycp_download" href="/report/xueli/survey.do?vcode=AUBGKX3N00G7H3BC" title="问卷调查" target="_blank" class="dcwjA">调查</a>
          </div>
        </div>
        <div class="newLayer" id="emailBox">
          <span class="newLayerArrow" style="right:45px;"></span>
          <a href="#" class="newLayerClose" title="关闭"></a>
          <table border="0" cellpadding="0" cellspacing="6">
            <tr>
              <td align="left" colspan="2">发送报告到指定邮箱：</td>
            </tr>
            <tr>
              <td><input type="text" name="toEmail" class="input_text input_t_l" id="toEmail" value="" /></td>
              <td><input type="button" value="发送" class="btn_blue emailButton" id="emailButton" /></td>
            </tr>
            <tr>
              <td align="left" colspan="2"><span id="emailMsg">&nbsp;</span></td>
            </tr>
          </table>
        </div>
        <div class="newLayer" id="xxewm" title="学信二维码">
          <span class="newLayerArrow" style="right:1px;"></span>
          <a href="#" class="newLayerClose" title="关闭"></a>
          <div class="alignC">
            <img src="/report/img/463432068e478d75889c4445859c1f6146b0957330.jpg" alt="学信二维码" /><br />
            <a target="_blank" class="bindGA colorBlue" href="/xlcx/downloadxxewm.do?id=63432684787588944585916146095733&amp;ln=CN">下载</a>
          </div>
        </div>
      </div>

      <div id="resultTable">





        <div class="tableTitle">
          教育部学历证书电子注册备案表
          <br>
          <div class="xlzms-tit">

            <span class='zbrq-title'>更新日期：2022年3月26日</span>
          </div>

        </div>
        <div class="div1">
          <div class="div2">
            <table width="628" border="0" align="center" cellpadding="0" cellspacing="0" class="cn_table">
              <col width="91">
              <col width="172">
              <col width="91">
              <col width="140">
              <col width="133">
              <tr>
                <th>姓名</th>
                <td colspan="3"><img class="by_img" src="/report/img/463432068x478d75889c4445859c1f6146b0957330.jpg" width="402" height="43" /></td>
                <td rowspan="4"><div class="cn_photo1" id="xueli_photo_div"><img src="https://t1.chsi.com.cn/chsi/images/report/xl/photo_cn.jpg" width="132" height="175" /><img class="cn_photo1_img" id="xueliPhoto" src="/report/img/463432068l478d75889c4445859c1f6146b0957330.jpg" width="120.0" height="160.0" /></div></td>
              </tr>
              <tr>
                <th><div style="width:90px;">性别</div></th>
                <td><span id="xb" style="width:166px;">男</span></td>
                <th><div style="width:90px;">出生日期</div></th>
                <td><span style="width:134px;">1995年09月06日</span></td>
              </tr>
              <tr>
                <th>入学日期</th>
                <td><span>2015年09月13日</span></td>
                <th>毕(结)业日期</th>
                <td><span>2019年06月25日</span></td>
              </tr>
              <tr>
                <th>学历类别</th>
                <td><span>普通高等教育</span></td>
                <th>层次</th>
                <td><span>本科</span></td>
              </tr>
            </table>
            <table width="628" border="0" align="center" cellpadding="0" cellspacing="0" class="cn_table cn_table_noborder">
              <col width="91">
              <col width="302">
              <col width="101">
              <col width="133">
              <tr>
                <th><div style="width:90px;">学校名称</div></th>
                <td><span style="width:296px;">曲阜师范大学</span></td>
                <th><div style="width:100px;">学制</div></th>
                <td><span style="width:128">4 年</span></td>
              </tr>
              <tr>
                <th>专业</th>
                <td><span>软件工程</span></td>
                <th>学习形式</th>
                <td><span>普通全日制</span></td>
              </tr>
              <tr>
                <th>证书编号</th>
                <td class="cn_font2"><span>1044 6120 1905 0042 20</span></td>
                <th>毕(结)业</th>
                <td><img class="by_img" src="/report/img/463432068b478d75889c4445859c1f6146b0957330.jpg" width="132" /></td>
              </tr>




              <tr>
                <th>校(院)长姓名</th>
                <td colspan="3"><span>张洪海</span></td>
              </tr>






              <tr>
                <th style="height: 200px;">在<br />线<br />验<br />证</th>
                <td colspan="3">
                  <table border='0' cellpadding="0" cellspacing="0" class="table_zxyz">
                    <colgroup>
                      <col width="170">
                      <col width="250">
                      <col width="150">
                    </colgroup>
                    <tbody><tr>
                      <td >
                        <div class="vcode-block" style="width: 170px;margin-right: 10px;">
                          <span class="cn_font2 vcode-detail">AUBGKX3N00G7H3BC</span><br>
                          <span class="vcode-title">在线验证码</span>
                        </div>
                      </td>
                      <td>
                        <div>
                          <img src='https://t3.chei.com.cn/chsi/images/yzbg/mini-program.jpg' width="130"/>
                          <span><img class="icon-mini" src='https://t1.chei.com.cn/chsi/images/yzbg/mini01.png' height="12" title="微信扫一扫，使用小程序" alt="微信扫一扫，使用小程序"/></span>
                          <span>1、扫码获取“学信网报告在线验证”<br/>小程序</span>
                        </div>
                      </td>
                      <td>
                        <div class="bg_ewm_div">
                          <img src="/report/img/463432068q478d75889c4445859c1f6146b0957330.jpg" width="110" class="bg_ewm" />
                          <span><img class="icon-mini" src='https://t2.chei.com.cn/chsi/images/yzbg/mini02.png' height="12" title="小程序扫一扫，在线验证" alt="小程序扫一扫，在线验证"/></span>
                          <span>2、使用小程序扫码验证</span>
                        </div>
                      </td>
                    </tr>
                    </tbody>
                  </table>
                </td>
              </tr>
              <tr>
                <td colspan="4">
                  <h2>注意事项：</h2>
                  <div class="zysx">
                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                      <tr>
                        <td valign="top">1、</td>
                        <td valign="top">备案表是依据《高等学校学生学籍学历电子注册办法》（<a href="https://www.chsi.com.cn/jyzx/201408/20140829/1245955796.html" target="_blank" style="text-decoration:underline;">教学[2014]11号</a>）对学历证书电子注册复核备案的结果。</td>
                      </tr>
                      <tr>
                        <td valign="top">2、</td>
                        <td valign="top">备案表内容验证办法：①点击备案表(电子版)中的在线验证码，可在线验证；②登录中国高等教育学生信息网“在线验证系统”，输入在线验证码进行验证；③使用“学信网报告在线验证”的微信小程序，进行扫码验证。为防止出现假冒报告，请使用该小程序扫描验证，不要用其他第三方扫描程序。</td>
                      </tr>
                      <tr>
                        <td valign="top">3、</td>
                        <td valign="top">备案表内容如有修改，请以最新在线验证的内容为准。</td>
                      </tr>
                      <tr>
                        <td valign="top">4、</td>
                        <td valign="top">未经学历信息权属人同意，不得将备案表用于违背权属人意愿之用途。</td>
                      </tr>
                      <tr>
                        <td valign="top">5、</td>
                        <td valign="top">报告在线验证有效期由报告权属人设置（1~6个月），其在报告验证到期前可再次延长验证有效期。</td>
                      </tr>
                    </table>
                  </div>
                  <div class="logoBot">
                    <img src='https://t1.chei.com.cn/chsi/images/logo.png?v=20171229' height="30" align="right" />
                  </div>
                </td>
              </tr>
            </table>
          </div>
        </div>







      </div>





      <script src='https://t2.chei.com.cn/chsi/js/report/print_en_2019.js'></script>


      <script src='https://t2.chei.com.cn/chsi/js/report/send_email_cn_1.0.1.js'></script>



      <script src='https://t3.chei.com.cn/chsi/js/util.js'></script>
      <script src='https://t1.chei.com.cn/common/js/snsshare-1.0.1.js'></script>
      <div id="share"></div>
      <script>
        var s = new SnsShare("share");
        s.show();

        $(function() {
          $("#bindGA_print").click(function(){
            $("#bgdy").toggle();
            $("#bgxz").hide();
            $("#emailBox").hide();
            $("#xxewm").hide();
            $("#noenreport").hide();
            return false;
          });
          $("#bindGA_download").click(function(){
            $("#bgxz").toggle();
            $("#bgdy").hide();
            $("#emailBox").hide();
            $("#xxewm").hide();
            $("#noenreport").hide();
            return false;
          });
          $("#showEmail").click(function(){
            $("#emailBox").toggle();
            $("#bgxz").hide();
            $("#bgdy").hide();
            $("#xxewm").hide();
            $("#noenreport").hide();
            return false;
          });
          $("#openxxewm").click(function(){
            $("#xxewm").toggle();
            $("#bgxz").hide();
            $("#bgdy").hide();
            $("#emailBox").hide();
            $("#noenreport").hide();
            return false;
          });
          $(".newLayerClose").click(function(){
            $(this).parent("div").hide();
            return false;
          });

          $("#showEmailEn").click(function(){
            $("#emailBoxEn").toggle();
            $("#xxewmEn").hide();
            return false;
          });
          $("#openxxewmEn").click(function(){
            $("#xxewmEn").toggle();
            $("#emailBoxEn").hide();
            return false;
          });
          $(".newLayerClose").click(function(){
            $(this).parent(".newLayer").hide();
            return false;
          });

// ga事件参数设置，参考：http://jira.chsi.com.cn/wiki/pages/viewpage.action?pageId=8651194
          $( ".openSample" ).live("click",function() {
            gtag('event', 'barcode_usecaseclick', {
              'event_category': 'onlinereport',
              'event_label': 'cn',
              'value': '1'
            });
          });

          $(".bindGA").click(function(){
            gtag('event', 'download_barcode', {
              'event_category': 'onlinereport',
              'event_label': 'cn',
              'value': '1'
            });
          });
          $(".bindGA_en").click(function(){
            gtag('event', 'download_barcode', {
              'event_category': 'onlinereport',
              'event_label': 'en',
              'value': '1'
            });
          });

          $("#go_bindGA_print").click(function(){
            doPrint();
            gtag('event', 'print', {
              'event_category': 'onlinereport',
              'event_label': 'cn',
              'value': '1'
            });
          });
          $("#bindGA_print_en").click(function(){
            doPrint();
            gtag('event', 'print', {
              'event_category': 'onlinereport',
              'event_label': 'en',
              'value': '1'
            });
          });
          $("#go_zycp_print").click(function(){
            gtag('event', 'print_zysurvey', {
              'event_category': 'onlinereport',
              'event_label': 'cn',
              'value': '1'
            });
          });
          $("#go_zycp_download").click(function(){
            gtag('event', 'download_zysurvey', {
              'event_category': 'onlinereport',
              'event_label': 'cn',
              'value': '1'
            });
          });
          $("#go_bindGA_download").click(function(){
            gtag('event', 'download_pdf', {
              'event_category': 'onlinereport',
              'event_label': 'cn',
              'value': '1'
            });
          });
          $("#bindGA_download_en").click(function(){
            gtag('event', 'download_pdf', {
              'event_category': 'onlinereport',
              'event_label': 'en',
              'value': '1'
            });
          });

          $("#emailButton").click(function(){
            sendEmail("/report/xueli/email.do?vcode=AUBGKX3N00G7H3BC&amp;rid=63432684787588944585916146095733&amp;ln=cn")
            gtag('event', 'email', {
              'event_category': 'onlinereport',
              'event_label': 'cn',
              'value': '1'
            });
          });
          $("#emailButton_en").click(function(){
            sendEmail("/report/xueli/email.do?vcode=AUBGKX3N00G7H3BC&amp;rid=63432684787588944585916146095733&amp;ln=cn")
            gtag('event', 'email', {
              'event_category': 'onlinereport',
              'event_label': 'en',
              'value': '1'
            });
          });


          $( ".sr_tab_title > li" ).live("click",function() {
            index = $(this).parent().children("li").index(this);
            $(this).addClass("onread").siblings("li").removeClass("onread");
            $(".sr_tab_cnt_toggle").children("div").eq(index).show().siblings("div").hide();
          });

          //照片水平垂直都居中
          var imgLeft = ($("#xueli_photo_div").width() - $("#xueliPhoto").attr("width"))/2;
          var imgTop = ($("#xueli_photo_div").height() - $("#xueliPhoto").attr("height"))/2;
          $("#xueliPhoto").css({"left":imgLeft+"px","top":imgTop+"px"});
        });
      </script>


    </div>
  </div>
</div>



<div class="outer-footer foot" id="footer"><a href="https://chesicc.chsi.com.cn/zxgw/zxjs/201604/20160418/1529506207.html" target="_blank">中心简介</a> － <a href="/about/about_site.shtml" target="_blank">网站简介</a> － <a href="/about/contact.shtml" target="_blank">联系我们</a> － <a href="/zhaopin/index.jsp" target="_blank">招聘信息</a> － <a href="/about/copyright.shtml" target="_blank">版权声明</a> － <a href="/ad/index.shtml" target="_blank">网站宣传</a> － <a href="/help/" target="_blank">帮助中心</a> － <a href="/z/tenyears/index.jsp" target="_blank">学信十周年</a> － <a href="/about/ct16.shtml" target="_blank">大事记</a><br />
  客服热线：010-67410388　<span id="kfEmail">客服邮箱：kefu#chsi.com.cn（将#替换为@）　</span>Copyright © 2003-2022 <a href="https://www.chsi.com.cn/" target="_blank">学信网</a> All Rights Reserved<br />
  主办单位：<a href="https://chesicc.chsi.com.cn/" target="_blank">教育部学生服务与素质发展中心（原全国高等学校学生信息咨询与就业指导中心）</a></div>
<script type="text/javascript">
  function footerPst(id1,id2){
    var subH = document.documentElement.clientHeight - document.body.offsetHeight;
    if(document.getElementById("footer") && document.getElementById(id1) && subH > 0){
      var leftH = document.getElementById(id1).offsetHeight;
      var rightH = 0,new_subH = 0;
      if(document.getElementById(id2)){
        rightH = document.getElementById(id2).offsetHeight;
      }else{
        if(leftH<443){
          new_subH = subH - (443 - leftH);
        }
        leftH = (leftH > 443) ? leftH : 443;//for news,news_right changed, the number change
      }
      if(leftH > rightH){
        if(leftH==443){ //说明leftH小于443，上面已经重新赋值了
          subH = new_subH;
        }
        document.getElementById(id1).style.height = leftH + subH - 20 + "px";
      }else{
        document.getElementById(id2).style.height = rightH + subH - 20 + "px";
      }
    }
  }
  window.onload = function(){
    footerPst("leftH","rightH");
    footerPst("leftMenu","rightCnt");
    footerPst("leftHeight","");
    if(window.location.href.indexOf("xlrz")>-1){
      document.getElementById('kfEmail').style.display='none';
    }
  }
</script>
<script type="text/javascript">
  $(function() {
    //弹出打印等窗口
    $("#openerHref").click(function(){
      $("#noenreport").toggle();
      $("#bgxz").hide();
      $("#bgdy").hide();
      $("#xxewm").hide();
      $("#emailBox").hide();
      return false;
    });
  });
</script>
</body>
</html>

Process finished with exit code 0

"""
# print(html_text)

res = etree.HTML(html_text)
# //*[@id="resultTable"]/div[2]/div/table[1]/tbody/tr[1]/td[1]/img

res = str(res.xpath('normalize-space(//div[@class="div2"])')).replace(" ","")
print(res)



# print(sex)
# print(date_of_birth)
# print(admission_date)

# def certificate(code):
#   r = requests.get('https://www.chsi.com.cn/xlcx/bg.do?vcode=%s' % str(code))
#   #
#
#   print(r.text)
#
#
# code = 'AUBGKX3N00G7H3BC'
# certificate(code)
