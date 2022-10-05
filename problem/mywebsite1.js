window.onload=getData()

function getData(){
    fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json").then(function(response){
        return response.json();
    }).then(function(data){
        let newList=data["result"]["results"];
        
        let divPromotion=document.querySelectorAll(".promotion")
        

        //上方2張圖文
        for(let i=0; i<2; i++){
            //景點首圖top_pic
            let top_pic="https"+newList[i]["file"].split("https")[1];
            //景點標題topTitle
            let topTitle=newList[i]["stitle"];

            //建立圖片相關標籤
            let twoPic=document.createElement("img"); //新增img標籤
            twoPic.setAttribute("src", top_pic); //給予img標籤 屬性及內容
            
            //建立景點標題標籤
            let twoTitle=document.createElement("div"); //新增div標籤
            twoTitle.setAttribute("class","promotion_text"); //給予div標籤 class屬性(要與原先在css中設定的名稱相同)
            twoTitle.textContent=topTitle; //將景點標題加入標題內容
           
            //將圖文依序放入
            divPromotion[i].appendChild(twoPic);//根據指定的class名稱,將新創的title div依序放入;(appendChild()不會覆蓋原本的資料,是會附加在子節點的尾端)
            divPromotion[i].appendChild(twoTitle);//根據指定的class名稱,將新創的twoTitle div依序放入
            
        }

        //8張圖文
        newList.splice(0, 2); //從索引0開始 刪除2個元素
        function picture(j){
            //景點首圖first_pic
            let first_pic="https"+newList[j]["file"].split("https")[1];
            //景點標題pictitle
            let pictitle=newList[j]["stitle"]; 

            //建立圖片相關標籤
            let viewImg=document.createElement("img"); 
            viewImg.setAttribute("src", first_pic);             

            //建立景點標題標籤
            let title=document.createElement("div"); 
            title.setAttribute("class", "pic_title");
            title.textContent=pictitle;  
            
            let divPic=document.querySelectorAll(".pic")
            //將圖文依序放入
            divPic[j].appendChild(viewImg);
            divPic[j].appendChild(title);
        }
        
        for(let j=0; j<8; j++){
                picture(j);
        }

        let loadMore=document.getElementById("btn")
        let gallery=document.querySelector(".gallery")

        function create(){
            let newdiv=document.createElement("div");
            newdiv.setAttribute("class", "pic");
            gallery.appendChild(newdiv)
        
        }        

        loadMore.addEventListener('click', function(){
            for(let k=8; k<16; k++){
                create();
                picture(k)
            }
            
            
        })
    })
}