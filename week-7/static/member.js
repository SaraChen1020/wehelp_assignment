const usernameSearchBtn = document.querySelector("#usernameSearchBtn");
const renameBtn = document.querySelector("#renameBtn");
const resultDiv = document.querySelector(".result");
const statusDiv = document.querySelector(".status");

usernameSearchBtn.addEventListener("click", function () {
  let username = document.querySelector("#username").value;

  fetch("http://127.0.0.1:3000/api/member?username=" + username)
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      let memberInfo = data.data;

      if (memberInfo != null) {
        resultDiv.textContent = `${memberInfo.name} (${memberInfo.username})`;
      } else {
        resultDiv.textContent = "無此資料";
      }
    })
    .catch(function (error) {
      console.log("error", error);
    });
});

renameBtn.addEventListener("click", function () {
  let newname = document.querySelector("#newname").value;

  fetch("http://127.0.0.1:3000/api/member", {
    method: "PATCH",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ "name": newname }),
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      if (data["ok"]) {
        statusDiv.textContent = "更新成功！";
      } else if (data["error"]) {
        statusDiv.textContent = "更新失敗";
      }
    })
    .catch(function (error) {
      console.log("error", error);
    });
});
