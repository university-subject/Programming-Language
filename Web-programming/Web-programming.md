# Web Programming Note
collected & noted by JIngShing

## HTML
input 輸入框
type = "text"
type = "submit"
type = "reset"
```
<form method = "post" action = "link.com">
   <p>
     <label>color:
         <input type = "color" autofocus/>
         (Hexadecimal code such as #ADD8E6)
     </label>
   </p>
   <p>
     <label>date:
         <input type = "date"/>
         (yyyy-mm-dd)
     </label>
   </p>
   <p>
     <label>Email:
         <input type = "email" required/>
     </label>
   </p>
```
* post隱藏
* get出現在頁面上
HTML1
-------
* 多選 checkbox
* 單選 radio
* 選單 select
  * 預設 selected
  * 選項 option
-------
"\#" is id

id = "bug"

\<a href = "#bug">
