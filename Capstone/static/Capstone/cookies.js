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
       const consentPopup = document.getElementById('consent-popup');
       const acceptBtn = document.getElementById('accept');

       const acceptFn = event => {
       SaveToStorage(StorageType);
       consentPopup.classList.add('consent-popup-hidden');
       console.log(consentPopup.classList);



       };
       acceptBtn.addEventListener('click',acceptFn);


if (ShouldShowPopup(StorageType)) {

    setTimeout(() =>{
            consentPopup.classList.replace('consent-popup-hidden','consent-popup');
            consentPopup.classList.add('text-warning');
            console.log(consentPopup.classList);
}, 1500);

}



};
