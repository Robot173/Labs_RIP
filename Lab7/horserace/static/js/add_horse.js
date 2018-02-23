/**
 * Created by Robot 173 on 16.01.2017.
 */

function validateName() {
    var y = document.forms["addhorse"]["horse_name"].value;
    if(y.length==0){
        document.getElementById('id_horse_name').innerHTML = "*Не бывает лошади без клички";
        return false;
    } else {
        document.getElementById('id_horse_name').innerHTML = '';
        return true;
    }
}

function validateOwner() {
    var y = document.forms["addhorse"]["horse_owner"].value;
    if(y.length==0){
        document.getElementById('id_horse_owner').innerHTML = "*Укажите хозяина";
        return false;
    } else {
        document.getElementById('id_horse_owner').innerHTML = '';
        return true;
    }
}

function validateClub() {
    var y = document.forms["addhorse"]["horse_club"].value;
    if(y.length==0){
        document.getElementById('id_horse_club').innerHTML = "*Укажите спортивный клуб";
        return false;
    } else {
        document.getElementById('id_horse_club').innerHTML = '';
        return true;
    }
}

function validatePicture() {
    var y = document.forms["addhorse"]["horse_picture"].value;
    if(y.length==0){
        document.getElementById('id_horse_picture').innerHTML = "*Прикрепите картинку лошади";
        return false;
    } else {
        document.getElementById('id_horse_picture').innerHTML = '';
        return true;
    }
}

function validateHorse() {
    if(validateName() && validateOwner() && validateClub() && validatePicture()) return true;
    else return false;
}