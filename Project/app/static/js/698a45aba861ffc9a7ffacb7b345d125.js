(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('彭泽县', {"type":"FeatureCollection","features":[{"type":"Feature","id":"360430","properties":{"name":"彭泽县","cp":[116.56438,29.876991],"childNum":3},"geometry":{"type":"MultiPolygon","coordinates":[["@@@@@A@@@A@A@AB@@A@A@@@@A@CB@@AA@@@@BAAABC@@@A@A@@@@@@@ABC@@@AB@@AA@@@A@@@A@@BA@A@@@@@@BA@@BABA@@@A@@BA@@@CB@@A@AACBAB@BA@@@AB@@AB@@AA@@@@AB@A@@A@A@@@@@A@@@A@@BAB@@CA@@AA@@A@@@@A@@ABA@@B@@@B@@A@@@ABCBA@@AAB@@@B@@@@A@@B@@@D@B@@B@@B@B@@@B@@ABA@@@A@@@@B@@@@@B@@@@@B@@@BA@AB@@AB@@A@ABCBC@AB@@@@A@@@A@AAA@@AA@@@@AC@AAE@@@A@@B@@AB@B@BA@AAA@@@@@A@@@@@ABA@@B@@AB@BA@AB@@A@@@A@@@@@BA@@AA@A@@@A@@A@@@@BA@@BA@@@AB@@@@C@@AAD@@A@@@@@@@AB@B@@@@@@@BA@A@AA@@@BA@@@AA@@@@@@AA@@A@A@@@A@@BA@@B@@AB@BCD@@A@@B@@@B@@AB@@A@@@AA@@A@@@A@@BA@@@@D@B@@@@@B@BAB@B@@BD@BA@@BAB@@AB@@AB@@@@@B@B@B@@@@@B@@@B@@@@@B@@@@A@AB@@A@AAABA@@@CA@@@@AA@@@@@@@B@@@@@@BB@@A@@@@BB@@BABA@A@@@AAA@ABA@CAA@@AA@CC@@A@CCAA@@A@A@AA@@A@A@@@A@@A@AAA@@AAAA@@@A@@@AAA@A@@A@CAAA@@ABE@A@CA@@A@@@@AA@A@AACA@@C@@AA@@B@@CAAAA@A@A@C@C@A@@A@@C@CAC@@@A@@A@@A@A@@B@AA@A@@@@A@@A@A@@@A@AA@@@@C@A@A@AAA@A@@@@A@@A@A@AA@@@@ABA@AAA@@AA@AAAA@A@@AACA@A@@AAAA@@A@C@AD@F@@@@EBA@@B@B@B@BEHCD@BCB@@@BCA@@@B@B@@@@@BAB@@ABABB@@@BBBBDBB@@B@@@BBBB@@@@BB@@BB@FB@B@@B@@B@@A@A@A@@@@@A@@@A@@@@@BB@@ABA@@BC@A@CBA@CDA@@@@BABA@A@@B@@@B@@DB@B@B@@D@@@BB@@@BA@@@A@@@A@AA@@@@A@A@@@@A@@A@@@@@A@A@@BA@@B@@@@AB@@@B@@@B@@A@A@@@@@@A@@@@A@@@ABA@A@@@AB@@@@@B@@@BA@@BA@@B@@@B@@AB@@A@A@@@@B@BBBBB@@B@@B@B@@D@BB@B@@AB@@@@DB@BB@@@@BBDBB@B@B@BB@BDB@@@B@BBB@BBBB@@BBBB@@BBBB@@@@@BBB@B@@D@@B@@@@@B@B@@BBB@BB@@BABA@@@AB@BA@@B@@@B@D@BBB@D@B@@@@@BA@ABE@@BAB@@AB@B@DBB@@B@@@B@B@B@@BBABB@@B@@@BB@BB@@@B@@AB@@@@CBA@@BA@@B@@@@BD@@BDB@@B@@@BBBBB@BB@@BAB@@B@@B@@B@BB@@@BAB@@@BBF@D@@CB@@A@@B@@AB@D@@@BA@A@A@A@AB@@AB@B@BAB@B@BBB@BBB@@@B@B@@@BA@@@@B@@A@@B@B@@@BBD@@@@@B@@@@@BB@ADBF@@AB@B@B@@ABA@@@AB@@@B@@@D@B@@AB@B@@@@@B@@@@@BB@@@@B@@@@@@A@@B@@A@@B@D@B@B@@A@A@@@C@@BB@@BA@A@@@A@A@A@AAA@AA@@@B@@@@BB@@@@@B@DA@@B@@BBA@@B@@AB@B@@@@B@@@BBB@@@BB@@@BB@@@A@BBB@@@@B@@@@@BA@@@@@@@@@@@@B@@@@B@@@B@@@@@@@@@@A@@B@@BBA@@@B@@@B@@@@B@@@B@@B@B@@@B@@@@@@@@AB@@@@@@@@@B@@@B@@@@@@BB@@@@@@@@@@@@@@@B@@B@@@@@@@@@@BA@@@EB@B@@@BA@@@@@A@@@A@@@@B@@BFB@@BBD@@@BBB@B@B@B@BAB@B@B@B@@@@A@@A@@@A@@@A@@AB@@@@C@A@A@@BA@A@@@A@@BBBA@BBDD@BB@@BBAB@@BBBB@@B@B@@@BBBDB@@@@@B@D@@AB@@@B@@@@@B@@@@ABA@@BAAABEA@@ABA@@@A@AA@@AB@@A@@@AA@AAB@@@@@BAB@@@BCB@@CB@@A@B@@BBBB@BB@@BBBD@D@BB@BBDB@@B@@B@BABAF@@@BCH@BE@@@rVDBNHXLJDLJLF\\RLBNBP@R@dAXBLB@@F@NFLH@@JHHTFJBL@BJfBLD\\Fd@DATD`L`HRHNBBT\\PNNHTDHBfFH@J@TBJAPCXGDAXMD@NGLELCLANBD@ZFLOHAJBD@DCDEBGBE@CDCDADCJ@BBDABGFMFIFIDGDCBABI@ABA@@B@@@D@DBFBHDJDHDHDF@D@BC@ECCAC@A@ABA@@@A@A@@BC@C@AAABC@AA@AA@C@@@A@A@@@AAA@@@@DA@@@AAA@C@A@ABA@A@A@A@A@A@A@AB@DGB@BAB@@@B@BB@B@BCB@@@B@B@D@DBF@@@@H@B@D@DAB@@@BBDBB@@@FDFBFFHDDBB@HBDCHCRIJE@ADCDCDCBCBABABEBEBE@GAICGCECEAG@E@A@GEQEI@CCGAIACGKEECCGGEEEIEEAACEIIGEA@GGCCEEGCIGAAACCEKOEMAECCCEAAEGKEGCEEECCCCA@@ECKAEBCBCDEFCDMBG@KIEEGG@ACIACAGCIKIKAECCAECAEIE@@ACEGIOECAACAA@KCEAAACAACCG@ACGAAEICGCE@CCCAGEEIACAGACACC@A@CBGDCT@NDHEFE@ABA@GAGEEECUQEEGECGEGAE@ABGFEB@FCFCJEHCFEHEFCBCDAFEBGOIA@@@A@A@@@@A@@@A@@CA@A@@AA@@@@ABA@@@@@@D@@A@CB@@@@A@@A@@A@@B@@@B@@@BA@@@@A@BA@@@@@@B@@@B@@B@@@@@@@AB@@@AAAA@@@B@@AA@@BA@@@@@A@@@@BABAB@@AB@@A@@@@@AAA@@@@@@@A@A@AB@@A@@@A@@A@@@AB@@AAAA@@@A@@@@A@@@@AABA@@@ABA@C@@@@@A@@@A@AA@@AAA@@@@A@@AA@@@@@BA@@@A@A@A@@@A@@@A@@BA@@B@@AAA@@@AA@A@@A@@@@@A@A@@@A@@A@A@@@@@AB@B@@@@@B@@@@@@CBA@@B@A@@A@@A@@C@A@C@@@@BA@@@@@A@A@ABA@A@@CB@AAABA@A@A@@@@@B@@AB@@@@AAB@@@@A@@@A@@@@A@@@@@B@@@@@@A@@@@@@@@@BB@@@@@@@@@B@@@@B@@@@BA@A@@@ABA@"],["@@AABA@@AA@@@@A@@@@AAA@@@@A@@B@J@@ABAB@@AB@B@@@B@@@@@@AD@B@@@B@@B@B@BBB@B@@C@A@@@A@@@@@@@AB@@@@@@A@A@@B@@A@A@ABA"],["@@@ACC@AA@GDAB@@@@@ABA@@@@A@C@A@AA@@@@AB@@@BB@@BB@@@AB@BBB@@@D@@@B@@BBD@@@BAB@D@DBB@@A@@@ABC@@@C"]],"encodeOffsets":[[[119419,30295]],[[119508,30413]],[[119519,30405]]]}}],"UTF8Encoding":true});}));