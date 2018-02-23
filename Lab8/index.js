/**
 * Created by Robot 173 on 12.01.2017.
 */
var graf;
$('.plot').click(function (e) {
    clearInterval(graf);
    console.log(graf);
    var x = parseFloat($('.from').val());
    const x1 = x;
    var i = x;
    var step = 1;
    const x2 = parseFloat($('.to').val());
    const delta = 100 * (x2 + x1)/(x1*x2);
    const fun = ($('.fun').val());
    var poinst = [x, eval(fun)];

    console.log(poinst);
    console.log(fun);

    graf = setInterval(function () {
        if (x < x2) {
            $.plot($('.graph'), [{label: fun, data: poinst}], {});
            x = x + (x2 - x1) / delta;
            console.log(poinst);
            if (poinst.length > delta) {
                poinst= poinst.splice(1)
            }
            poinst.push([x, eval(fun)]);
            i += parseFloat(step)
        }
        else {
            clearInterval(graf);
        }
    }, 10);
});