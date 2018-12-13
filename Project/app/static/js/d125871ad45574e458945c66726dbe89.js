(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('钟山县', {"type":"FeatureCollection","features":[{"type":"Feature","id":"451122","properties":{"name":"钟山县","cp":[111.303009,24.525957],"childNum":1},"geometry":{"type":"Polygon","coordinates":["@@@@@@B@BA@@DA@@@@@A@A@@A@@A@A@@@@A@A@CBAEC@AAAAAC@C@AAA@@@CB@@CA@AAAAA@AAAAA@A@CAA@A@E@AAA@AAACCCA@C@A@C@C@@@AA@@G@@@CAABABA@A@@A@@AA@AA@A@ABA@A@@B@B@@@BAB@BBB@B@BA@A@@DAD@@ABAB@@A@AAABAAA@AC@AAAA@@BC@@@AAA@@@@BBB@@A@@@A@@@@AA@A@@D@B@B@@ADA@ABCBABBBA@@B@B@@@@@B@@A@@B@B@B@@@BB@@BABBB@@A@ABA@@BABABCBA@A@@@@@AAAAAAC@ACA@@AA@AAEAAAAAECA@@@CA@@A@@@A@AAABA@A@@@A@AAA@@A@@AA@@EA@DABAD@BADCB@DBBD@ABA@A@@BADCBCDCAEB@B@@ABABA@CA@C@@ACCAEAABAD@DBDBBAD@@A@EA@@@@AA@BA@@@A@A@@@@A@@C@A@A@ABA@A@EAGBC@I@EACCAAAAAB@B@@@B@BA@@BA@@@@B@@AB@@@@AB@@@B@@@@@B@@@BGF@DABABABC@@BCDABA@AAG@@AC@A@AA@@A@E@A@ABEAC@@BE@A@C@CBE@EABA@ACEA@ABC@CD@AE@C@ABCA@@@AC@A@AAAAA@@@@C@@A@@AAA@@CCAA@AAA@@AAAA@@A@@@A@AB@A@@@@AAA@@BE@A@@@C@A@A@@AABA@A@C@C@@@@@@A@@@AB@@A@@@AAABA@@@@@@@A@A@@@ABA@A@A@@@A@A@@@@@A@@@@@A@C@A@@@@@A@@@@AA@AA@@A@@@ACCAD@DABCAE@ABG@C@EAC@C@EFC@AD@@@@@BBDBD@DAFBDAB@BAF@D@@AFFBDBAB@@BDB@AB@BC@@@ABA@CA@@G@GAG@C@C@C@@CCCA@@BA@@FA@@@@@A@@@AB@@@@ABAA@@A@@@A@@@@@AB@@@A@@A@A@@@@@A@A@@@AA@@@AA@@C@GCCCAC@AB@CE@@AA@@@ABA@A@AD@DCAAB@@C@CCAB@BABEAABICADA@C@C@@B@@@@@D@BBB@BAB@@AD@@@D@B@@@@@@@BB@@BBB@@A@@B@@@@AD@@@@A@@@@AAB@@@B@@@B@@A@@@ABA@ABA@@B@@@@AA@@A@C@@@A@A@@BAAA@@@C@A@@@CB@@AAABA@A@G@EBA@GBA@CDAB@BC@EBAAABE@@@EBAB@BA@AB@@AB@@ABADA@EBAD@BDBB@DB@BDBHED@HCHAFBBBD@BDA@@BB@B@B@B@BB@@BD@B@B@B@@BB@DB@@B@BBBAB@B@BBBBB@B@@@BBB@@ABBBBB@DDBBBF@BB@B@@@BBB@@@@BB@@DB@@@@@BB@BBBB@@@@BB@@@@BB@@@B@BB@BB@@@B@@B@BBBB@BDDBBBBBB@@@@@BA@@BCBBB@B@B@D@@@B@@AB@@@BA@CAA@@@@@BBAB@@BBAB@@@@AB@B@B@BBD@@@B@@@BB@@@@@BB@BBB@B@@D@@BB@@B@@@AD@BCBAB@BBD@B@BB@B@@BB@@@BH@@ABAD@BB@BAB@BBB@@CDADABB@F@@BADD@BB@DE@ABAD@@@BAB@D@B@DA@@@A@CBA@@D@@ADC@AB@@ABDB@DABB@@BF@B@@@@AB@@@B@B@@B@@@B@@DB@B@@AD@@BBB@@@DCBABB@@D@D@BBBD@D@@@@A@@BA@C@@@@@@BA@AB@BA@@B@BAF@@@@@@@@AB@@A@ABC@@@@B@@@@@B@@A@@@A@@@@BB@@@BB@@@BABA@CFC@@B@@C@C@@@A@@@@DC@@BA@@@AB@B@@ABCB@@A@BDA@BB@@@BAB@B@BAB@@ABBBAB@B@B@BAB@@@BB@@D@@BBAB@B@@@B@BDB@BA@@@EDCB@BABEBAAGBABEBCBA@A@C@@DAD@BDBCBAFCBCB@BBFEBADEBBD@D@D@BDBB@FDB@@BBBA@@B@@@B@@@B@@@@BBB@@@@BB@@@@BB@@@BBB@@B@@@BB@DAB@@@B@@@@BBB@BB@@@@BB@@B@@BB@@@BB@@@@@DB@BB@@@@BBB@@@B@@@@ABA@@B@@@@@BA@A@@@@@A@@@ABAAA@@BAACB@@A@A@@@A@@BA@@@@@A@@BA@A@@@@B@B@D@B@@@@BB@B@BAB@@@@ABBDAB@B@B@B@@@BHAB@DBB@B@FABBB@B@BBDB@D@BBF@HFAB@DBB@@BAFDDBB@@@B@FBD@@H@@DAB@@DD@BBBB@@BA@AFABBBBB@@BB@BBB@@BD@@BB@@B@F@DDB@B@DA@@FD@@B@B@DAHA@CB@@@B@@AB@B@B@DD@@@@DB@@D@BBB@BBB@B@B@@BBBBB@@@BF@@DB@DDB@@B@@@B@@A@@@AB@BB@@@@B@@B@@BBB@B@@B@@@B@@@@@BBB@@@B@@@BB@@B@@@@@@B@B@@B@@B@B@@B@@DBB@@@B@@@BB@@@B@@@@BAB@@B@@BB@@B@@DABAB@DAD@FBDBDAB@B@D@BJCDBFADCBAD@BAB@FBDBDDBB@F@DDDBHAB@BBBADADDDAHCADB@@BBB@BLFBHBD@BBBABB@@DBB@FDBBBFD@DDFDDB@@B@DBB@D@BDB@BBDB@@@BAD@JCDAFADB@@B@B@@@B@@@B@@@BA@@BABAB@D@@@@@AI@C@GAGGIBADEBEDE@C@EBG@CBCDABC@@BA@A@@@@@@@A@@B@@AD@@AAABABA@@A@@@@A@@B@B@DBB@@@B@BBDBBAB@B@B@@A@@@@DA@@@BBA@AB@@@BABABE@CDADE@AB@@@BA@@BA@C@@ACB@@A@A@@@@@C@@B@D@@@@@@BBBD@B@B@@@@AB@@@BADI@EBEFCDAFCF@@ABCHEDICACE@CECBEBAHARCPCPAJGL@LDBHHH@@BB@BDBD@F@DBBA@CBADCDCDCJB@CB@F@BABAD@@@BBDBB@B@@B@BDABA@ABAFBB@@A@C@CAC@ABAAEACACBCBA@ABC@C@ABC@A@ABA@CAAACBACCA@BEDA@C@@@A@CDAB@D@@@B@BB@BBBBBB@D@BA@AB@AA@AAA@CACBCDGA@DEBEBACIAA@ACAAAAACACACAA@CACEABAA@@A@AEAA@ACC@@@AD@BAB@BA@A@@BA@ABA@A@@B@@A@@BAA@@ADEB@@A@@BA@A@@@@BAA@@@BA@A@A@@B@@@BA@ADCF@B@B@@CB@BBBABAB@FB@BD@BADCBCDCB@@ABCB@BBBBBDB@BABBB@@@@ABAB@@AAA@EC@CCCDC@A@A@CAAA@CAA@CAC@AA@ACE@CB@@@@EDB@ADA@GAAA@AA@@@CB@@CCDAAABAB@FEB@AACA@ADA@ABCDABC@A@AAACBE@@BB@DBEBCBCB@ADCAAABCCAA@ACAG@AG@@@A@@@EAIACBA@ABCBCBCAAB@B@DA@@BAD@BBB@B@@@BADA@@D@B@D@B@B@@AB@B@@@@@AAAAA@@ABA@@@A@@DBBAF@DBB@@@DABC@A@AAACCCA@AB@@A@@@@@AACCA@@AA@AB@@@BC@@B@B@@@DA@@B@BA@ABA@@D@HCBBBABAFABA@@B@B@BA@@B@@@BCBAB@@ABBDAD@BAB@B@B@B@BAB@@AD@@ABABA@AD@BAB@DBFCB@D@BADBD@DCB@B@@@BABABABABA@@BCD@B@B@D@@@@@BADCACDC@@@AAAAA@A@@ACAA@A@A@@@A@@@ABA@AB@@@@A@A@@@@@A@AA@AA@@AA@@@A@@@@BAAA@@A@@AA@@@@A@@A@BAA@@A@A@@@@AA@@@A@A@A@@@@@A@@@A@@@@@AB@@A@@@A@@B@@A@@@@A@@C@A@@@CB@@@@A@@@@@A@@@@A@@@@A@A@@AA@AA@@A@AB@@A@A@@A@A@@@@A@@A@@BAA@BA@@AA@AA@@@@AB@@@@A@@A@@@@@A@A@@@A@A@@BA@@@@@@@AB@@@AA@B@A@@A@@@AA@@@AA@@A@@@A@@@@@A@@@@@A@@@@@AA@@AA@@@@AB@@@@A@A@@FAB@@@@@@@AA@@@@@@@A@@@@@@@AA@@@@A@@@A@AA@BA@@CA@AAD@B@@@B@@A@AA@@ABA@A@@@@@@@AA@ACA@A@@@@@A"],"encodeOffsets":[[114081,24903]]}}],"UTF8Encoding":true});}));