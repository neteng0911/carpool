const cookieStorage = {
    getItem: (key) => {
        const cookies = document.cookie
        .split(';')
        .map(cookie => cookie.split('='))
        .reduce((acc, [key, value]) => ({...acc, [key.trim()]: value}));

    return cookies[key];

    },
    setItem : (key, value) => {
    document.cookie = `${key}=${value}`;
    },



};




const StorageType = cookieStorage;
const ConsentPropertyName = "cookie_consent";
const ShouldShowPopup = () => !StorageType.getItem(ConsentPropertyName);
const SaveToStorage = () => StorageType.setItem(ConsentPropertyName, true);


window.onload = () => {
    if (ShouldShowPopup()) {

        const consent = confirm('Agree to the terms and conditions of the site?')
        if (consent){
            SaveToStorage();

        }


    }



};
