(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('伊春区', {"type":"FeatureCollection","features":[{"type":"Feature","id":"230702","properties":{"name":"伊春区","cp":[128.907257,47.728237],"childNum":1},"geometry":{"type":"Polygon","coordinates":["@@CCUKECOG_KOCK@IDKJSVCJQ^@JAHANAB@@@BBP@NH`JVJPLPJLHDDBVBN@HDDDBBBBB@JCFCJ@LFHDBEDCJEBCBIHEHEDCLAFDLHDDFJHHLAAMISKGAEDELAJ@FCBIIEGEQCGEII@@JMH[AM@CKKUKUO"],"encodeOffsets":[[132013,48837]]}}],"UTF8Encoding":true});}));