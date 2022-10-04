**Техзадание:**
*Когда турист поднимается на перевал, он фотографирует его и вносит нужную информацию с помощью мобильного приложения:*

* координаты объекта и его высоту;
* название объекта;
* несколько фотографий;
* информацию о пользователе, который передал данные о перевале: имя пользователя (ФИО строкой); почта; телефон.

*После этого турист нажимает кнопку «Отправить» в мобильном приложении.*

___

**Реализация:**
*1. Создать базы данных*
*2. Создать класс по работе с данными*
*3. Создать REST API c одним методом — POST submitData*

*Мобильное приложение вызовет метод submitData REST API.Метод submitData принимает JSON в теле запроса с информацией о перевале.*
*Метод submitData принимает JSON в теле запроса с информацией о перевале. Ниже находится пример такого JSON-а:*

{
  "beauty_title": "пер. ",
  "title": "Пхия",
  "other_titles": "Триев",
  "connect": "", // что соединяет, текстовое поле
 
  "add_time": "2021-09-22 13:18:13",
  "user": {"email": "qwerty@mail.ru", 		
        "fam": "Пупкин",
		 "name": "Василий",
		 "otc": "Иванович",
        "phone": "+7 555 55 55"}, 
 
   "coords":{
  "latitude": "45.3842",
  "longitude": "7.1525",
  "height": "1200"}
 
 
  level:{"winter": "", //Категория трудности. В разное время года перевал может иметь разную категорию трудности
  "summer": "1А",
  "autumn": "1А",
  "spring": ""},
 
   images: [{data:"<картинка1>", title:"Седловина"}, {data:"<картинка>", title:"Подъём"}]
}
