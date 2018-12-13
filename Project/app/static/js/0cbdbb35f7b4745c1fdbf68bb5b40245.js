(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('罗源县', {"type":"FeatureCollection","features":[{"type":"Feature","id":"350123","properties":{"name":"罗源县","cp":[119.549776,26.489558],"childNum":1},"geometry":{"type":"Polygon","coordinates":["@@@@@BB@@@@@BB@@@B@@A@A@@@ABABA@A@@@@B@@AA@@@@CAA@@A@A@@@@@A@@A@A@@AAA@@@A@A@@@@C@AA@@AA@@BAA@@@AAA@A@A@A@@@A@@BCBA@@BA@@@BB@B@@ABABA@A@AB@@@@@B@@BBB@DBBBB@@BBB@B@B@BADB@@@@@@@BB@@B@@BB@@@B@@@@@B@@BB@@B@@@@A@@@@@BB@@@@@B@@@@@B@@@@ABA@@@A@CBA@@@A@A@A@@@ABAB@B@@@B@B@@@B@@@@AB@@BBAB@@AAA@CB@B@@A@@AC@CCCA@AA@AA@@A@@@A@A@@@CA@@AB@@A@A@AAA@A@@B@@B@@BBB@@@B@@@@A@@BAB@B@@@BB@@@B@@BB@@@B@BB@@@BBB@@@BB@BB@@BBB@@@@B@@@BB@A@A@@@A@@@A@@@A@A@@@@@@@A@@B@@@@@@@@@@A@AAAA@@A@@AA@AA@@@@CA@@@@AA@A@AA@@@A@CAC@@A@@@@A@@@A@@@@A@AAA@@A@@@C@@@@@A@C@@@A@AB@@B@@BA@@B@BABA@@@@B@@BB@@@B@B@@A@@AA@@@A@A@@@AAA@A@A@AB@@@@CAEAA@C@AAC@@AA@AB@@C@AACAAA@AA@@AAA@@@@@AB@@@@A@@AA@@@A@@@@CA@@A@@A@@AA@A@@@AA@@A@@A@CBA@A@@@A@@@A@A@ABAB@@@AA@@@AA@@A@@ACCAAA@AA@@@@C@@@@AA@A@@A@@A@A@A@C@@@@@CAA@@@A@A@AB@@@@@B@@ABCAABEB@@@BA@@@A@@@A@A@@@@@A@@B@@@@CA@@A@@@@@A@@@@@@A@@@AA@@@A@@@A@@@@@AA@@A@@@AA@@@@AA@@A@@@A@@AA@@BA@@B@B@@AB@@@B@@BB@@@BB@@@@B@B@@@@A@@B@@@@B@@B@B@@AB@B@@@BAB@@A@@@ABA@@BCA@@AB@@A@AAA@@@@@A@@B@@C@@@@@ABAB@@B@@@BBB@@BBB@@BBBB@B@@@B@@@@AD@@@B@B@BB@@BBB@B@@AB@B@BA@@@@@@@@D@B@B@B@@@@@B@@@@A@A@A@A@A@@@A@A@@@@@AA@@BA@@AA@ADG@@A@A@A@A@@@CAAA@@A@A@AB@BA@@@@A@@AA@@A@@@@@A@A@@@AB@BAA@@@A@@AAAA@A@@A@@BA@@B@BA@@@C@@@A@AA@@A@@@@AB@@@@A@AAA@@AAA@@@AAA@@@AA@@A@AAA@A@A@A@C@@@@@@@@AB@B@B@@@@A@@@@C@EAC@@AA@A@AAA@A@C@C@A@@@ABAD@@A@AB@@@BABCD@@A@@@CAA@AAC@@AAB@@A@@@@BA@@@AB@@@@A@@@A@@@@@A@@@@@A@ABA@@BA@@@A@@@A@@AA@A@@@@@A@@@A@CA@@@@A@A@A@@@@A@A@@AA@@AA@@A@A@A@AA@@@ABA@@A@@A@@@A@A@@AA@@AAA@@@A@A@A@@@A@A@@A@@@A@A@@BC@@AA@ABAB@@A@@BA@A@@AA@@@AGD@@A@@@ABC@@@A@@@@@@B@@@@@@@@@@@B@@@@@@@@@B@@@@@@@B@@B@@@A@@B@@@B@@@@@@@B@@@@@@@B@BBBABBB@@@@BBBB@@D@B@@@BAB@B@@@@BB@@@@@B@@@@BB@@@@@@B@@@@BB@@@B@@B@@B@@@B@B@@@B@@A@@@@@@@@A@@@A@AAA@@@@@AA@@AAAA@@@A@C@@@A@A@A@@@AA@@A@@A@@@@A@@@@@@A@@A@@A@A@@@A@A@@@E@A@A@@@C@AA@@@@@@B@B@B@BBD@B@@@B@@A@A@@@AA@@@@@AAAB@BA@@@@@AC@@AAA@A@AA@@C@@A@A@@@A@@@AC@@A@@@CAADAD@@@@CBAB@@AAA@@@@@A@AB@@A@@@@BA@@AA@@AA@C@@A@@@@@@A@@@@@@AA@@@@@@@@@@BBBA@@AA@A@@@@@@AAC@@A@A@@A@@@A@A@A@@@@A@@@A@@@A@@@@B@@AA@ACA@@@@@ABA@@A@A@A@@@@@AA@@A@@BAD@B@@CDA@ABA@ABA@@@@BA@@BABA@ABADA@A@AB@@C@@@A@@@AB@BAB@B@B@@@B@BABAB@@ABA@A@@@@BAB@@@@@@EA@@@@CBAB@@@@ABA@ABA@C@ABA@A@@B@@B@@BAB@@BB@@@B@B@B@B@B@@@@C@C@@@AB@@A@A@C@A@A@AB@@C@ABCDA@ABCBCB@B@@A@A@CDA@A@@@A@@@ABA@AB@BC@ABA@AB@@A@A@@BCBABA@ABAB@@BB@@@@F@B@DB@@@B@@B@DB@@BBBBB@@@@@B@B@B@B@@BB@@B@@@BBB@@B@BBBB@@AB@@@@@DBB@@@DA@@B@@A@AB@@A@@@GDA@A@@@A@@BA@@DA@@@CBAB@B@B@@ABCB@@A@@B@BA@A@@B@@A@@@AAA@EAA@E@A@@BAB@@@@@@@@@@@BA@@A@@@@AB@@@@A@@@@B@BA@A@A@@@A@@@@BA@@@AB@@A@@@BB@@A@@@@@@@A@@@A@A@A@@@@B@@@@@@A@@@@@@B@@@@@@A@A@@@@@ABA@@B@@@@@B@B@@@B@@@@AB@@@BA@AB@@@@A@@B@@@@@@@B@@AB@@@@@BB@@B@ABB@@@@BB@@@B@B@@BB@@@@@BA@@@@@A@A@BBB@@@B@@B@@@BA@@B@@@B@@@@@B@BBBBB@B@@B@@@@@@@@B@@@@@@@@@@@@@@@@@B@@B@@@@@@@@@@@@@@@@@@@@B@@@@@@B@@@@@@@@@@@@@@@@B@@@@@@@@@@@@@@@@@@@@BB@@@@@@@@@@@B@@@@@@@@@@@@@@@@@@B@@@@@@@B@@@@@@@@@@@@@@BB@@@@@@@@@@@@@@@@@@@@B@@@@@@@@@@@@@@@@AB@@@@@@@@@@@@@@@B@@@@@@@@@@@B@@@@@@@@@@@@@@@B@@@@@@@@@@@@@@@@B@@@@@@@@@@@@@@@@@@@@@@@@B@@@@@@A@@@@@@@@@BB@@@@@@@@@@@@@@B@@@@B@@@@@@@@@B@@@@@@@@@@@@@B@@@@@@@@@@@@@BB@@@@@@@@@@@@@@@@B@@@@@@@@@@@@@B@@@@@@B@@@@@@@@@@@@@@@@@@@@@@@@@@B@@@@@A@@B@@B@@@@@@@@@@@@@@@@@@@@@B@@@ABAB@@@B@@B@FBBB@DBD@B@@@BA@@BAB@BA@@D@D@@@B@@BB@@AB@@@B@B@@B@@@B@B@B@BBB@@@@@BB@B@@BB@BB@@@@B@@@DA@@@@@BD@B@B@DBB@@@BDB@B@@BB@B@@AB@@@B@@BB@@@@B@BAB@@@B@@BB@B@@ADB@@@@BB@F@@B@@BB@B@BBB@@@B@@@@BB@BBB@@@BB@@@@AB@@@DABABAB@BAB@@@DABA@@BA@A@@@A@C@@BA@@@AB@@A@@@ABA@@@@B@@A@A@@A@@@@A@@@@@@@@@@@@@@DC@@@@@A@@BA@@B@B@@ADA@@@@@@B@@@B@@@@BB@@@@@@@@@@@@@@@@@@@@@@@@AB@@@@@@@@@@@AA@ACAAC@@@A@@A@@AA@@ABA@ABA@@@@@@@A@@@@B@BAB@@@@@B@@A@@BA@@@@B@@A@@@A@@@A@@BA@@BCBABA@@B@@@@@D@@A@@B@@@@B@@@@D@@A@@B@@B@@@BBBBB@@@@B@@@@@B@@@D@@@B@@@B@@@DB@@AB@@BB@@@@B@@B@@B@B@B@@@BD@@@@@B@@BB@B@@BB@@AB@@@BBB@@AB@@B@DB@BB@@B@@@BBB@@@BBB@@@B@BB@@@@@BAB@B@B@@A@@@@BAB@@@@@@AB@@@B@@@B@@@@A@A@@B@BA@@BB@ABB@@@@B@BABC@@@@BAB@DAB@@AB@A@A@@ABA@@@@B@@@@@@A@@@@@@@@@@B@@@D@BB@@BA@@BB@@AD@@AB@B@BBD@B@@@B@D@B@@@BBBBB@B@B@@AB@@@B@@B@@@@B@BB@@BA@@B@B@@@@@B@@@@@D@@@B@@BBBB@B@@AB@BB@@@@B@@@B@@@DB@BB@@BA@@DBB@@@@B@BA@@@@B@B@@@@ABA@@D@B@@B@@BB@@@B@@@B@@@@BB@@@@DBBBB@@D@@ABBDB@BBBB@BBBBDBB@DBB@@@@BBB@@@A@A@@@@B@D@@@B@@@B@@@@@BA@@@@BA@@@A@AA@@A@@@A@@B@@@B@@@@@@@B@BA@AB@@AA@@C@@AA@@@A@@B@BABA@BB@@@@@B@BD@@DBB@@@B@BB@@@@BAB@BA@@B@@@@@BBB@@B@@@B@B@@@@B@B@BB@@BB@B@@B@@@B@BA@@D@B@@@BDBBB@@@@@@B@BAB@@ABCBA@@@@@@@BBBB@@A@@B@@BB@@B@B@@@B@B@@@BABA@@@@@B@B@@@D@D@@B@@@BAB@B@@@B@B@B@BA@@AA@@B@B@@A@@BB@@B@@@B@B@B@@@B@B@@@B@@@@BB@@AB@B@@@B@DB@@@@AB@@BBB@@@@BBB@B@BBB@@@@B@@@@@@B@@BBBB@@@B@@BB@B@@AB@@@B@@@B@B@B@B@@@@BB@BB@@@@@B@B@B@B@@@B@BBB@@@B@@@BA@@DB@@BA@@BBB@@AB@BA@@BA@@B@F@B@BAB@@@B@@ABAB@@@@@@ABB@@@@@@BBB@@@@@BB@@@@@@BBB@@@@@B@BB@BA@@BB@@@@@A@ABE@A@@@@B@@@BA@@@A@@@CBA@@BA@@@A@@@@@A@@@AD@@A@B@@BB@DB@@@AB@@A@@@@@@B@B@BB@@@B@@ABAB@@@@BBB@@@@BB@@@B@BADB@@@@BA@@BA@@B@@@B@@@@AB@@@@A@@@@@A@@@A@@BA@@@@@@BA@AB@@@@@DA@@D@@@@A@@BA@@@B@BB@B@B@AA@@B@B@@BBABB@@@@@@B@D@B@B@B@BBB@B@@@BB@BB@B@B@B@@B@@@@@DB@@@@@D@B@B@@A@@B@@B@@B@@@@@B@@@@A@@D@@@@A@@B@B@B@D@B@B@@@B@@@B@@AB@@@@@B@@AB@@@F@@BB@@@@B@BB@B@@BB@@@@@BAB@BABAB@@@B@@A@@DAB@BAB@BA@@D@@@B@@@B@@@B@@A@A@@@AA@@@@A@@@@D@B@BA@BB@B@@@BA@@D@@B@@BB@@B@B@BA@@@ABA@@BA@ABA@@BAD@B@@@@A@@@@AA@@@@@A@AB@AA@@@A@@@A@A@A@@B@@@@@AA@@B@@AB@@AB@@A@A@@AA@A@@@A@@D@FBB@@@BA@A@@@@@@BA@@@@BABA@@@@@A@@@@BA@@@A@A@@@@B@D@BADA@@B@@@@@BA@A@@AA@@@AB@@@BAB@@ABABA@@@A@@@@@A@@@A@@@@@@AA@@A@AAA@@@@@@A@@A@@@A@@@A@@AA@BAB@@A@@@@@@B@@@B@B@@A@@@@@@@@@A@@B@@A@@@A@@@ABA@A@@@A@@BAB@@AB@@AB@B@BA@@B@B@B@D@BBB@@@@A@@B@@@@AB@@@@ABA@@@@B@B@@BB@@AB@@@DAB@B@@@B@@@BAA@@AB@@A@A@A@AA@@A@@@AB@@A@@AC@@@@B@B@B@B@@@@@BBBBBABB@@B@B@@@DCBAB@@@DCBA@@BAB@DB@@@@B@@@BBD@B@B@@@@@BABA@A@@@@@A@A@@B@B@@@B@B@@@B@@A@@@@B@@@BBB@@BB@@B@@B@@B@@BBB@@@DB@@@@BB@@B@@A@@@A@@@@AC@A@@@@B@@@BBB@@A@@B@@AA@@AB@B@D@BA@@@@B@@AB@AA@C@A@@@@B@DA@@B@@A@A@@@@@@@A@@B@@@B@@@@@@@B@B@B@BBBABA@A@@@AA@AA@@@@@@@@@@B@@ABA@@B@B@B@D@B@@BB@@@B@DB@@B@BBD@BB@@BB@BB@@@@@BBB@B@@@B@BA@A@@BBB@@@@BB@@@BBBAB@BABADA@A@@B@BBBB@A@@@@@@@@BB@B@B@@@AB@@@B@@@@@@A@@BA@@B@B@@@B@@BB@@@@@@BB@@@A@@B@@ABB@@@AB@@BB@@@B@BBB@B@@B@@B@@@@B@BA@@@@BB@@B@BA@@B@@A@@B@@@D@BBBBD@@B@BBB@@B@@@@@@B@@@@@@BB@@@B@BA@@B@@@B@B@@B@@@BD@B@@B@@@@B@@@@@B@@@@@B@@B@@BA@B@@D@@@B@@BD@DBB@@@@@@BB@@@@@@BBBB@@DB@@B@@@BA@@@@D@B@@@B@@B@@@@B@BBBB@@@@BB@BB@@B@@D@FB@@FA@@@@AA@@B@@@@AB@@CB@BA@@BBB@DBBBB@B@BCB@@A@A@@B@B@@BBAB@DAB@@@B@@AB@@@@AB@@@@@BA@@@@DB@BB@@BB@B@BB@@@AB@B@@BBBDDBB@@BBB@DDB@@B@@@@@@ABA@ABA@@@@B@@@@@BB@@@@@ABB@@@@BBA@@B@@@B@B@@@B@@A@@BA@BB@@@@BB@BAB@@@B@B@@BBBB@BABB@@B@DBBABB@@B@@@B@@@BA@A@@B@@@B@@AB@@@BA@@BAB@B@@@B@BA@@BA@AB@DAB@DCB@B@@ABBB@BAB@F@HKJGDK@A@AACJWHORgBEHYFQTuBCBIBGAICEBGBCWE]IEIAEGKaSgUsQI@UJ_`ILILSZCDCBYVUPMCKEA@A@@@@AA@@AAA@A@A@AAA@A@A@@AA@ABA@AB@@AB@@AAA@@@A@@@A@A@A@@@AA@@A@A@A@@@A@@@A@@@A@AB@@ABA@@ACA@@@A@AAA@CAA@C@A@AAABAA@@A@AAA@A@@@A@A@A@CBA@A@C@@AC@A@@AA@@@@AA@@@A@AA@@A@@@@A@@@A@@@A@@@@@@A@A@AA@@AA@A@@@C@A@@@ACA@@AB@AAA@@@@@A@@EA@AA@AAA@AA@AA@A@@@AAAAA@AA@@@A@@@@A@@@@@@@@@AA@@A@@@CA@@AB@@A@@@@B@@@B@B@@@@@B@@A@@@@@@B@@@@BB@@@@A@A@A@@@@@CAA@@@@BA@"],"encodeOffsets":[[122450,27022]]}}],"UTF8Encoding":true});}));