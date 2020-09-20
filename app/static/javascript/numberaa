function addFigure(numVal) {
    // 空の場合そのまま返却
    if (numVal == ''){
        return '';
    }
    // 全角から半角へ変換し、既にカンマが入力されていたら事前に削除
    numVal = toHalfWidth(numVal).replace(/,/g, "").trim();
    // 数値でなければそのまま返却
    if ( !/^[+|-]?(\d*)(\.\d+)?$/.test(numVal) ){
        return numVal;
    }
    // 整数部分と小数部分に分割
    var numData = numVal.toString().split('.');
    // 整数部分を3桁カンマ区切りへ
    numData[0] = Number(numData[0]).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    // 小数部分と結合して返却
    return numData.join('.');
}
/**
* カンマ外し
* 入力値のカンマを取り除いて返却
** [引数]   strVal: 半角でカンマ区切りされた数値
* [返却値] String(): カンマを削除した数値
*/
function delFigure(strVal){
    return strVal.replace( /,/g , "" );
}
/**
* 全角から半角への変革関数
* 入力値の英数記号を半角変換して返却
* [引数]   strVal: 入力値
* [返却値] String(): 半角変換された文字列
*/
function toHalfWidth(strVal){
    // 半角変換
    var halfVal = strVal.replace(/[！-～]/g,
    function( tmpStr ) {
        // 文字コードをシフト
        return String.fromCharCode( tmpStr.charCodeAt(0) - 0xFEE0 );
        }
    );
    return halfVal;
}

/** 
 * 処理を適用するテキストボックスへのイベント設定
 * onBlur : カンマ区切り処理実施
 * onFocus : カンマ削除処理実施
 */
var elm = document.getElementById('numdata');
elm.addEventListener('blur', function(){ this.value = addFigure(this.value) }, false);
elm.addEventListener('focus', function(){ this.value = delFigure(this.value) }, false);