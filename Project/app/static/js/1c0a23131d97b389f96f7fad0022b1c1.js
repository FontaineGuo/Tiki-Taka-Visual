(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('威远县', {"type":"FeatureCollection","features":[{"type":"Feature","id":"511024","properties":{"name":"威远县","cp":[104.668879,29.52744],"childNum":5},"geometry":{"type":"MultiPolygon","coordinates":[["@@@@A@@@@@A@B@@@B@@@@@@@@@@@"],["@@@@@@@A@@B@@@@@A@AA@@@B@@@@@@@BB@@@"],["@@AAE@CAAAA@AB@BAAA@CB@AAA@@C@@AABAB@@AB@@BDA@@@C@AA@@A@ABA@@B@@@B@@@@@@DAB@B@BB@@@@ABABAB@B@B@BB@@@B@@@BCB@@@B@@@@@@B@BAF@B@@@@EAAA@@A@@@@@AB@@ABAD@@A@@BAA@@AC@A@@@ABA@@@@A@A@@@A@@@@B@@@D@B@@AB@@A@@@C@@@A@@@B@BD@@@B@B@@A@AA@@A@@@@@AD@B@B@BA@@@A@@@AA@@@AB@B@@@@A@@A@CA@@@AB@BA@@@@AAAAA@@AA@@A@@AA@@@@AA@@A@@@@@@B@@BBBB@@@@ABA@@@AA@@AAAB@@A@@BBB@B@@@@A@A@AB@@@B@B@@BB@@B@B@@@B@@B@@@B@@A@A@CBA@CAA@A@AB@@@@@D@BB@B@D@B@@@@BAB@@ABA@@B@@BB@@@BAB@@B@@@DB@@@BA@A@E@@@ABA@@B@F@B@F@@@B@@A@AAAA@A@ABABC@A@@@@A@@@ABABC@@B@@@@BDA@@B@@@@AAAAABABA@@@@A@@@AA@@@A@@D@@@B@@BB@BA@@BA@AACAA@A@AB@@@@BBBB@B@B@@@BA@E@A@@BC@@B@@@BBB@BABA@ABA@AA@AAA@@A@A@ABAB@B@@@BB@BBD@@@AB@B@B@@@BD@@@@BA@@@A@CAA@@@@B@D@@@B@@@@A@@@@A@AA@@@AB@BA@A@@@@B@@@BA@CAA@A@@B@@@BBBCBBB@@@B@BAB@@@B@@@@ABA@@@@DA@@@AC@@A@A@AB@AA@AAA@@@@A@AA@@@A@@@@@@@@@BA@@@AA@A@@A@A@A@A@@A@@@@A@@DCB@@@@A@@AA@@@@ED@@A@A@@B@@@BA@@@A@@C@@A@A@@A@@@AA@@@ABA@C@A@@@@@AB@@A@A@@@@@@@BA@A@@A@AA@@@A@@B@B@B@@@@AAA@AA@AB@@@BAAA@AA@@@A@@A@@@@@@@@BA@AB@B@@ABA@@B@@A@AA@@A@@BA@@B@@@B@@@BA@A@@@@@@B@@@@B@@@@B@@@@ABABC@@BA@@@@D@@@BCB@@@@@BAB@@@@@A@AAA@@AB@@@B@@AAA@ACC@CAC@AA@@AE@AAAGBABA@A@AB@BADB@@BBD@BABA@ABAAE@@AAA@@@IAA@AA@@AAC@A@@DANE@A@@@CEAIAC@AAEAC@E@A@ABBFAF@DADCD@@AHADABABA@EBCBAB@@ABADAFAD@D@DA@ADB@@B@BF@B@D@F@DAD@JCD@BABAB@B@@@DABAHEBAB@B@B@BB@@@B@BAB@@CBABABE@ABA@@BA@@B@D@BBF@B@BBBDDBD@B@BA@@BA@BB@DBF@@@BAB@@A@G@A@AB@B@@BDDD@@@B@B@B@@CDAB@@@B@B@DBBALAF@HADAB@BAB@@BDBB@DABABCDEDA@EFCFCHGNIHIJ@@A@C@E@A@C@ABA@@@AB@B@F@BA@@BCBCDCD@B@@@BB@HBBBB@@BCH@HBB@D@BBBB@DB@@@@@@BB@B@B@DAB@BBF@DAB@BADABAB@B@BA@ABEBC@ABA@E@AB@@ABAFA@A@A@ABA@AAG@E@EAA@IECAAAC@A@@CA@AB@A@@AAA@A@ABABA@@@AAA@A@C@@BAD@B@@@@@BADAB@BA@ABCB@@E@A@A@@B@D@@@BABA@@@AAA@AAGCA@A@A@ABCBABCBADA@@BA@C@A@EBA@A@A@A@ACAACAACAA@@CCCEA@@AAA@A@CAG@ABAB@@AB@BA@A@@AC@AB@BABA@A@@@A@ACC@AA@@ACAA@GAA@A@AA@@AAAAAAACCCCA@@CAA@C@A@A@EECA@@C@AA@@AA@A@C@AA@A@A@A@A@@BA@CBCD@@ADAFAD@DAD@BAFAB@DA@@BCBA@@@ABAB@BADABA@@BA@E@GBA@A@A@AB@BAFAD@BAD@BBBAB@BA@A@ABA@@@EAEA@@C@C@ABCBA@AB@@QHA@A@CAECCACB@@ABAB@B@BB@D@D@B@F@@@B@@@@@AB@BCD@B@BB@AJ@DAB@BA@CB@@ABEDA@DBBBDBBB@BBFBB@BAD@BBB@@@BBBD@BB@@BB@H@BBDDDBB@BBBAD@BAD@BB@DABAB@B@BB@DBBBBDBBBBB@B@B@B@BBB@BD@@BB@@@BB@B@D@BBBBDDB@BBB@B@D@BB@BBB@DB@BB@@B@F@@BBDBB@BBBF@BB@@BDBDAB@HEBA@CBAFC@AFADAB@B@H@DBBBDBBBBB@FABAFIFA@ABCDA@CBABB@@DAD@@@BDBDBBBD@B@BBB@B@DBBBBB@B@B@BB@B@D@DB@B@B@BBBBBB@B@BABABAB@BB@BB@BBB@BAB@DCB@BDDFBBB@B@H@BBBBDBFBB@BBDBDBDBB@D@@@BABADGBC@CBABABA@AB@B@D@BABABAD@B@BBDBDBD@DADBFBD@DABAB@F@B@D@@B@B@BBD@BFDFBDBDBBBBBBDAB@F@FAB@FBB@DBBBHDFDHBBDFDFDH@@BBJABAB@FB@BBDB@B@DAB@B@FDBB@BBBBB@BF@BB@BBBDAFCHEBAB@@@DCD@@@BABADCBEDEBCB@@@D@@@B@B@B@B@@@B@BBB@B@BAB@L@DBDAFBB@B@HHDBB@B@F@D@B@B@@BB@FB@@DA@E@E@E@EB@B@B@DBB@BA@@@A@A@@B@BA@BB@@DBD@@B@B@BCB@@@B@B@BABCBA@A@ABA@AAA@AAA@ABEBC@@@A@CBC@ABA@@BAB@B@B@DBB@@@BBBBBDADADAFCFBBBDFF@@BBB@BBB@BBBBBDB@B@@@@E@ADCBC@@@ABAB@BA@A@A@@BAB@FBD@@BBDBB@DBBBBDH@@BBBB@BB@B@B@B@FAD@B@@@BA@A@CEKAA@C@CB@BA@A@@@A@@AE@@@A@@@CBABE@@BADADCB@D@@ABA@@@E@ABABCDADADCBCBADADAHIFBFDDDB@HBF@DC@GBO@CBCB@HMDIFGFQ@@CAAA@@AA@@AAA@GB@AA@@CBCFAB@@A@@@A@@@AB@@AAAAE@ABCD@N@BABI@IBA@IBI@ABMBGFMHOBAFGFGDEFCL@NCH@J@L@LBLAJAFCDABGFGBCDAD@B@DBDBDBF@HEBEDEHIDCF@L@L@D@H@JAH@LCHEAA@AB@DC@@@A@A@ABA@ABA@AAA@@A@A@@A@A@@BAB@B@B@BCB@DAB@@@@A@@AA@@BC@@ACA@BA@@D@@ADCBABA@ABA@@@@B@@B@D@BBB@@BBB@B@@AB@@AAA@E@@@ABA@@@@AAA@A@@@A@@@@AB@BADAB@B@B@B@@@@ABA@@BAB@BAB@@ABC@@@A@CA@@AAA@@@A@AEIGG@ACCCAAAE@CAABC@E@CBCDG@GAC@A@AACACACE@EFCDAB@@AB@@AA@@AB@BAB@@A@CCCACBCDCFADC@ABABEDEBAA@@A@AAAAAA@@AAA@C@A@ABA@A@AAAAA@A@C@AACAC@A@@ACA@ECA@@A@CBA@@@A@A@A@AAA@@AAABA@GFC@@BA@@F@D@B@B@D@@AB@BA@C@A@EAC@AAAD@BBB@BA@GFAB@BBF@@ABA@C@EDA@A@A@@AAA@@AACCAAA@@@A@CB@BABA@ABA@@@AA@@A@AACAACCEAA@@@@@@@AC@AB@BA@AAA@@@@@A@AA@@A@@ACBCA@B@D@@@B@D@BABCBABCDA@@@CAAA@AAA@@@AA@@@A@A@A@@@AAAA@ABA@@AA@A@@@AA@@A@A@@@A@A@@@@@@@A@A@@AA@@@@@@@@@A@@AAEACACA@A@ADAB@BBBBDBBBB@@@BA@A@AA@@AC@AA@@AA@@@ABAFEBC@@@AAAAA@@@A@@BAB@BBBBBB@@BA@@CE@A@G@AA@A@A@C@CB@@@A@A@@DADEB@B@BB@B@DBB@@DBB@B@DEAA@ACEEC@A@AB@BAB@B@DBB@BB@BAB@B@B@@BBB@HBB@BA@@@AAA@EAA@@AAEC@A@A@@BA@A@A@C@ACAACA@@A@@BAF@BC@AA@AA@AAA@CBE@@AA@@A@@@@@CAABA@ABABABEL@BABA@IAC@A@@AA@BADGBCBA@A@AA@@CBA@AFG@A@AA@AAAAC@AAABA@EDA@ABC@A@CBA@@@"],["@@@@@@@@@@@@@@@@@@@@@@"],["@@@@@@@@A@@@@@@@@B@AB@"]],"encodeOffsets":[[[107207,30386]],[[107206,30388]],[[107241,30070]],[[107301,30306]],[[107302,30305]]]}}],"UTF8Encoding":true});}));