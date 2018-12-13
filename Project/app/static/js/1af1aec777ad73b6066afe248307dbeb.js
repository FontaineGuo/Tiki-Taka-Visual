(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('西乡塘区', {"type":"FeatureCollection","features":[{"type":"Feature","id":"450107","properties":{"name":"西乡塘区","cp":[108.313494,22.833928],"childNum":2},"geometry":{"type":"MultiPolygon","coordinates":[["@@AA@A@APC@@B@BCCCGCCACA@CDCBEBGCE@A@@C@AAC@@A@AA@C@CBI@CBCBE@EAA@CDAFA@C@ABC@AAABA@@@A@CB@@GCC@AAC@A@A@CB@@@B@BA@@B@@AB@@CB@@AD@@@BB@B@@@FN@BBB@@@B@DB@B@AB@DBD@@@@@B@B@@@D@BBB@@@BA@@BAD@@AFIAAB@B@@@B@F@@@B@FEF@@@BC@GHA@A@A@@@C@C@C@@@O@AB@B@@A@@@AD@@CBA@A@C@A@@AA@@A@@EC@BA@A@MBABA@E@@B@@A@@BC@A@A@A@A@EAC@AAM@CBIAA@E@A@A@A@C@@AA@A@@@@BA@AB@@A@AB@DAB@@@BA@@B@@@BA@BD@@A@@D@DA@@B@@@@@@@BA@@BABA@A@@B@@ABA@AAA@A@A@AB@@ABA@@BA@A@@BCBABA@@D@@C@CDA@AAC@@BA@C@AAAAA@@@@AA@A@@@@@A@@@@@@@@@@A@@@@A@@@@@@@@@AAA@@@@@@@AB@@@A@@@@@@A@@@@@@@AA@B@A@@AB@@@@@@@@@@A@@@A@@B@@A@@B@@ABA@A@A@A@A@A@AAABABA@ABA@A@A@AB@@CDABA@AAA@A@@@A@AA@@C@A@CBA@A@AB@@@@AA@BAB@@C@AB@@ABA@AB@@@B@@@@@D@@BBABCBA@A@@B@@A@A@@@@@ABAB@@AB@@@@AB@@AB@BABABA@@B@@AB@BA@@B@D@B@B@@A@@B@@AB@@A@@@A@A@@@@@AB@@A@@@A@@B@B@B@BA@@BAB@@@B@@@@ABBADD@@@@B@@DB@@@B@B@BBD@B@@@BB@@B@@@@BBB@BB@@BBBFB@@B@B@@@DBB@@B@B@BHBB@@@@BB@@BD@B@@@BBB@@@D@D@D@B@BBB@@@B@B@B@D@B@@@BB@@@BB@BB@B@@@BB@@@B@B@B@DAF@F@DB@@@BBB@@@@B@@B@B@@@@AB@@ABAA@@@BA@@@AB@BBB@BAB@BB@@BB@B@BB@@AB@@DD@B@@B@@@B@@A@@BAAB@@ABB@@B@@@@@B@@B@B@@@B@@@BA@@B@@@@AB@@@B@AA@@A@@@B@@@AA@AAA@@B@@@@@B@B@DAB@@@B@B@B@@@BBB@@@BA@@@AB@@@@A@@A@@@@@A@@@@@@A@@@@A@@A@@@@BBD@@@@@BAB@@@@ABB@@@@@@B@@B@@BB@B@@@@BB@@B@@@@@@@B@@@@A@@@B@@B@B@@@B@@@A@@@A@@@@B@@BB@@@@@B@@B@@@@@@@BA@@@@B@@A@ADCBCAA@@@@AA@@@A@@FA@A@@@C@@B@BAB@@@@AB@@@@@B@@A@@@A@AB@@AD@@@BA@@@A@AB@@@BBBBB@B@BD@B@B@@@B@BAB@@@@@BB@@@@@@@B@@@DBB@@B@B@B@BBFBBB@DBF@B@@BDBB@@@FB@@BBBD@@@B@@BBB@@@@BDB@@D@@BBBB@B@B@@AB@@BB@BB@@B@@@@B@@@DBB@D@@BB@@@@BBDAF@@@B@B@@@BBB@@DB@@BBD@@B@@AB@B@@BB@@@B@B@@@B@@AB@@B@@B@@D@@B@BB@@@BBD@D@@@BBB@B@BABBB@@@D@@DB@BB@DB@@ADBB@B@A@@@BB@F@H@@@B@@B@@B@@@BB@@@@BBBBBB@@BB@BB@@@BB@BBD@B@@@@AB@@@@B@@BB@@@@@@BB@@@B@B@@@@B@B@@B@@@B@B@@@@@@B@@B@@@B@BBB@DBB@@@@B@@BB@B@@@B@@@@B@@@@@B@B@@@D@DAD@@@LVDL@@B@B@@BBA@@@B@@B@BB@B@@BB@@@@@B@@@@@AB@B@@@@@@@@@@B@@@@BB@@BB@@@@B@@@B@@@@BDB@@BA@@@@BB@B@@@BBB@@B@BA@@BBBBB@@@B@AA@@@A@A@A@@@ABBDDB@B@@B@@@B@@@@@B@@@B@@@BA@@@@@ABBBAD@B@@BB@@BB@@@DF@DABBB@B@BBB@D@B@B@FB@BBBB@@@BAD@@@B@B@@@B@D@B@@B@@@DADADB@BBD@BBB@@@BBB@@D@B@@AB@@@FB@B@@@B@@@B@@AB@DBB@@@B@B@B@B@D@@ABBB@@@@DB@@B@@@B@B@@B@B@BDB@D@B@@@BB@@B@B@@AD@@@B@@@B@BA@@B@@AB@B@B@DB@BBB@AB@@ABA@ABACAA@AA@@CBAA@A@AC@BAAA@A@AB@EAAC@A@A@@@AB@D@B@D@@@BAB@@BB@BA@@BA@@@AB@D@@AB@B@@A@@BAB@B@@A@A@@AC@@BA@@@AA@DABA@AB@BBB@B@@@BA@AB@B@B@DD@ABA@@@ABAB@@@B@B@B@ACB@AA@@A@@@A@@AA@@@@A@@@AAAC@@@@C@@@A@@@A@ABAB@@@BBB@DB@@@@B@B@BBA@@B@@@B@@BB@@BA@@D@@@B@@@B@@@BBB@@@B@B@@@B@BA@@B@@BB@@@@DB@@@BD@@@BDB@@BB@@BAB@@@B@B@BB@@@@B@@ABB@@BB@@B@@A@@B@@@@@@@B@BBB@BB@ABBB@BAB@DABB@AB@@A@@B@B@B@@AB@D@@@BA@AA@BAB@@@BB@@D@@A@C@@@@@A@AA@A@@@C@@@@A@@C@@@A@@B@@AAAA@@@A@@@@BA@A@@@ABADCBA@@@@@A@A@@B@BA@@BB@A@ABA@CAA@AAC@C@AA@@@@AB@B@B@D@@A@AB@BA@@@BB@B@BA@@A@@A@@@AB@@EBA@C@@AAA@@@@ABAB@F@@CB@B@DABC@ABAB@B@AA@AC@@AA@@@@@AA@@A@AA@@@@@AA@@@A@A@@@A@A@@@@@@@@@AA@@@@@@@@@@@AD@@A@A@A@AA@@@AAACAAA@A@@ACA@AAA@@BA@@B@BA@@@CAA@A@ABA@A@A@A@AA@@AA@@ABAA@AA@@BA@@@AB@@A@@@A@AAAAA@A@AAA@A@E@A@A@AB@BAB@BAB@BC@ABA@@@@B@@CB@BC@AC@A@A@@AAAC@EA@A@@BCBABA@A@A@A@ABAB@D@@ABA@A@ABA@@AAAACAIEA@AAAAEEA@BAB@JCBAB@@AD@D@DB@AFBB@DBDAB@BBDBBBDBJBBBBBDB@B@BA@@BABAF@BB@BBBB@BB@DB@BA@@BB@BBBBBAB@B@D@B@BBBB@BF@DBDBD@B@B@BAB@BABABADAB@D@@@B@@BB@B@@@@B@DBBBBBADBB@B@BABABAB@BA@@B@B@J@@@F@BAB@B@BD@B@B@BAB@BBB@@BDBDBBB@BBB@BB@BD@@BDB@B@@@B@B@B@BBBBBB@B@BAB@BBBBHBBBDABD@@BBHHB@@@DBhNDBDBB@RDD@@BHAHFF@DB@@@@@@FILABBB@B@@ABA@A@A@@AA@AA@@A@@@A@@AA@@BC@@@A@@@@@A@@@ABA@@AA@@@@@A@@@A@@@@@A@@@A@@B@BA@@@A@@AA@@BC@A@A@@BA@A@@BA@C@@@A@@@A@@ACACAC@A@C@@AABCAA@A@@@AB@@G@@@CBA@A@A@A@C@@@A@A@@@A@@AA@CDC@AB@@@@A@@C@CA@@BC@@A@@@A@@@@CDC@@@A@@A@AB@BAB@BAA@@AAAACC@AAC@@AAAA@A@A@@BECG@A@CCE@ACC@@EC@@BDAB@@B@@BB@EB@@@@A@@@@@AA@@A@@@@AB@@@@AAB@@@@@A@@@@@@A@@@@@A@@@@A@@@@@@B@@@@A@@@@@@B@@@B@@@@@@A@@@@A@@@@@@@B@@A@@@@B@@@@@@CBA@@@A@A@A@ABAA@@@@@A@@@AAA@@@A@@AA@@@@@@A@@@@@@@@@AA@@@@AB@@@B@@B@B@B@@BB@@B@BBB@A@BAA@@@@@B@AA@B@AA@@@@A@A@A@@A@@@B@@AA@B@@A@@@@@@A@@@@@A@@@A@@@A@AB@@@@@@@@A@@@BAA@@@@ABA@A@@@C@@@CBC@@@@@C@@@ABC@@@@@@@@@ABB@A@@BA@CA@@AACA@@@@ACA@@GAECCA@@@@BCCACA@@@@AAA@@@AAA@B@@C@@@ABA@A@@BAAA@@@@@@@AD@@A@@B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@A@@@@@@@@B@@@@@@@@@BA@@@@ACA@@@C@GAA@@@CCACA@@@AAACABAA@@CA@@EACA@@IFA@A@ABAB@@AB@@ABCBCD@@A@@BKJGF@@GH@@A@GFKB@@@@E@@B@AEB@@I@C@KAWEGAIA@@MA@@CAM@@@A@K@CCAABC@@@@@@@@JOBAHMBA@@FIAO@MAAKMKKUMC@A@MASDEBOLOLABMJebB@MJAJ@D@FJNJN@@LNFTABC@C@E@WSCCOCABEHAD@BG@GACA@@ICCFCJ@HCN@@CPEFAB@@E@AAECSUAACACAIG@A@A@A@@@@@AHEHDFNL@HG@IKEA@@BAA@@KCM@KGCEDKME"],["@@AACA@@AA@@A@@@@B@@A@AA@@A@@BA@B@@B@@@@@B@@@@A@A@CAA@A@@@AA@@A@A@@@@AA@@@B@@A@A@@@@A@BC@@BA@@@@AAA@@A@@AA@@C@@@A@@@ABAA@@@@A@@@A@@@@@@@A@@DCDADAB@@AD@@@BA@@AA@AA@CA@@A@@@A@A@@A@@@AB@@@@AD@@@F@BB@@B@@ABA@A@A@A@@B@@@BB@B@@BB@@D@B@BAB@@@B@@B@D@B@@@@AB@@AB@D@B@BABB@@@@@@@BCBA@A@@BABAB@B@@@BB@@@B@@@D@D@B@@@@@@@@@@BA@ABC@@@A@A@A@@@@@@B@@@@BBDB@BB@BCD@@@@@@BA@@B@@BBD@B@@B@BA@@B@@@B@@FD@DB@@@@BD@D@D@BB@A@AB@BA@@BA@@B@@AB@BABAB@@@FB@@B@@@B@@AB@@@B@BBB@@A@@@@@A@@@AB@B@@@B@BAB@@@B@B@BA@@@A@@A@CAA@A@C@B@BE@A@A@CB@@@B@CECC@@BAB@@A@@AA@A@AA@AA@@@AA@"]],"encodeOffsets":[[[110622,23361]],[[110600,23630]]]}}],"UTF8Encoding":true});}));