(this.webpackJsonpfront=this.webpackJsonpfront||[]).push([[0],{24:function(e,t,c){},25:function(e,t,c){},32:function(e,t,c){"use strict";c.r(t);var s=c(1),i=c(17),r=c.n(i),n=(c(24),c(25),c(10)),l=c(2),a=c(0),j=function(){return Object(a.jsx)("header",{id:"header",children:Object(a.jsx)("div",{className:"logo",children:Object(a.jsx)("a",{href:"/",children:"Unistats"})})})},d=c(18),o=c(7),h=function(){var e={"NaUKMA \u041d\u0430\u0423\u041a\u041c\u0410 \u041d\u0430\u0446\u0456\u043e\u043d\u0430\u043b\u044c\u043d\u0438\u0439 \u0443\u043d\u0456\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442 \xab\u041a\u0438\u0454\u0432\u043e-\u041c\u043e\u0433\u0438\u043b\u044f\u043d\u0441\u044c\u043a\u0430 \u0430\u043a\u0430\u0434\u0435\u043c\u0456\u044f\xbb":"\u041d\u0430\u0446\u0456\u043e\u043d\u0430\u043b\u044c\u043d\u0438\u0439 \u0443\u043d\u0456\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442 \xab\u041a\u0438\u0454\u0432\u043e-\u041c\u043e\u0433\u0438\u043b\u044f\u043d\u0441\u044c\u043a\u0430 \u0430\u043a\u0430\u0434\u0435\u043c\u0456\u044f\xbb","\u0423\u041a\u0423 UCU \u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0438\u0439 \u041a\u0430\u0442\u043e\u043b\u0438\u0446\u044c\u043a\u0438\u0439 \u0423\u043d\u0456\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442":"\u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0438\u0439 \u041a\u0430\u0442\u043e\u043b\u0438\u0446\u044c\u043a\u0438\u0439 \u0423\u043d\u0456\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442"},t=Object(s.useState)([]),c=Object(o.a)(t,2),i=c[0],r=c[1],n=Object(s.useState)(""),l=Object(o.a)(n,2),j=l[0],h=l[1];return Object(a.jsx)("section",{class:"forms",children:Object(a.jsx)("div",{class:"container-fluid",style:{width:"70%",margin:"0px auto"},children:Object(a.jsxs)("div",{class:"row",children:[Object(a.jsx)("div",{class:"col-md-12",children:Object(a.jsx)("div",{class:"section-heading",style:{float:"left"},children:Object(a.jsx)("h2",{children:"Search"})})}),Object(a.jsxs)("form",{method:"post",id:"contact",children:[Object(a.jsx)("div",{className:"col-md-6",style:{width:"100%",margin:"0px auto"},children:Object(a.jsx)("fieldset",{className:"center",children:Object(a.jsx)("input",{id:"name",type:"text",placeholder:"Type in some letters...",onChange:function(t){return function(t){h(t.value);var c,s=[],i=t.value.split(" "),n=Object(d.a)(i);try{for(n.s();!(c=n.n()).done;){var l=c.value;l=l.toLowerCase();for(var a=0,j=Object.keys(e);a<j.length;a++){var o=j[a];o.toLowerCase().includes(l)&&!s.includes(e[o])&&""!==l&&s.push(e[o])}}}catch(b){n.e(b)}finally{n.f()}r(s)}(t.target)},onKeyPress:function(e){return function(e){if(13===e.key)return e.preventDefault(),!1}(e)},value:j,class:"form-control"})})}),i.map((function(e){return Object(a.jsx)("input",{type:"submit",value:e,onClick:function(e){return h(e.target.value)}})}))]})]})})})},b=function(e){var t=e.data;return console.log(JSON.parse(t)),Object(a.jsx)("div",{children:Object(a.jsx)(h,{})})},x=function(e){var t=e.data;console.log(typeof t),console.log(t);var c=(t=JSON.parse(t.replaceAll("&#39;","'"))).student.first_name,s=t.student.second_name,i=t.student.mail,r=t.student.university;return Object(a.jsxs)("div",{className:"profile",style:{"margin-top":"100px"},children:[Object(a.jsxs)("h2",{children:[Object(a.jsx)("span",{children:"Name"}),": ",Object(a.jsx)("strong",{children:c})]}),Object(a.jsxs)("h2",{children:[Object(a.jsx)("span",{children:"Surname"}),": ",Object(a.jsx)("strong",{children:s})]}),Object(a.jsxs)("h2",{children:[Object(a.jsx)("span",{children:"Mail"}),": ",Object(a.jsx)("strong",{children:i})]}),Object(a.jsxs)("h2",{children:[Object(a.jsx)("span",{children:"University"}),": ",Object(a.jsx)("strong",{children:r})]}),Object(a.jsx)("div",{className:"col-md-6 col-sm-12",children:Object(a.jsx)("div",{className:"row",children:Object(a.jsx)("div",{className:"col-md-6",children:Object(a.jsx)("div",{className:"border-rounded-button",children:Object(a.jsx)("a",{href:"/logout",children:"Log Out"})})})})})]})},O=function(e){e.data;var t=Object(s.useState)("Student"),c=Object(o.a)(t,2),i=c[0],r=c[1];return Object(a.jsx)("section",{className:"contact-form",children:Object(a.jsx)("div",{className:"row specially-for-form",children:Object(a.jsx)("div",{className:"col-md-6",children:Object(a.jsxs)("form",{id:"contact",method:"post",children:[Object(a.jsx)("div",{class:"col-md-4 col-sm-4",style:{margin:"10px 0px"},children:Object(a.jsxs)("div",{class:"circle-item",children:[Object(a.jsx)("input",{name:"Status",id:"demo-small",type:"radio",value:"Student",onClick:function(e){console.log(1),r(e.target.value),console.log(e.target.value),e.target.checked=!e.target.checked},checked:"Student"===i}),Object(a.jsx)("label",{for:"demo-small",children:"\u0421\u0442\u0443\u0434\u0435\u043d\u0442"})]})}),Object(a.jsx)("div",{class:"col-md-4 col-sm-4",style:{margin:"10px 0px"},children:Object(a.jsxs)("div",{class:"circle-item",children:[Object(a.jsx)("input",{name:"Status",id:"demo-medium",type:"radio",value:"Enrollee",onClick:function(e){console.log(2),r(e.target.value),console.log(e.target.value),e.target.checked=!e.target.checked},checked:"Enrollee"===i}),Object(a.jsx)("label",{for:"demo-medium",children:"\u0410\u0431\u0456\u0442\u0443\u0440\u0456\u0435\u043d\u0442"})]})}),Object(a.jsx)("div",{className:"col-md-12",children:Object(a.jsx)("fieldset",{children:Object(a.jsx)("input",{type:"text",name:"name",placeholder:"Name...",required:!0})})}),Object(a.jsx)("div",{className:"col-md-12",children:Object(a.jsx)("fieldset",{children:Object(a.jsx)("input",{type:"text",name:"surname",placeholder:"Surname...",required:!0})})}),Object(a.jsx)("div",{className:"col-md-12",children:Object(a.jsx)("fieldset",{children:Object(a.jsx)("input",{type:"password",name:"password",placeholder:"Password...",required:!0})})}),"Student"===i&&Object(a.jsx)("div",{className:"col-md-12",children:Object(a.jsx)("fieldset",{children:Object(a.jsx)("input",{type:"email",id:"email",size:"30",placeholder:"University email",required:!0})})}),"Enrollee"===i&&Object(a.jsx)("div",{className:"col-md-12",children:Object(a.jsx)("fieldset",{children:Object(a.jsx)("input",{type:"email",id:"email",size:"30",placeholder:"Email",required:!0})})}),Object(a.jsx)("div",{className:"col-md-12",children:Object(a.jsx)("fieldset",{children:Object(a.jsx)("button",{type:"submit",id:"form-submit",class:"button",children:"Register"})})}),Object(a.jsx)("div",{className:"col-md-12",style:{"margin-top":"20px"},children:Object(a.jsx)("div",{className:"border-rounded-button",style:{width:"20%",margin:"0px auto"},children:Object(a.jsx)("a",{href:"/login",style:{"text-decoration":"none"},children:"Login"})})})]})})})})},u=function(e){e.data;return Object(a.jsx)("div",{className:"main",children:Object(a.jsxs)("div",{class:"inner",children:[Object(a.jsx)("section",{class:"main-banner",children:Object(a.jsx)("div",{class:"container-fluid",children:Object(a.jsx)("div",{class:"row",children:Object(a.jsx)("div",{class:"col-md-12",children:Object(a.jsx)("div",{class:"banner-content",children:Object(a.jsx)("div",{class:"row",children:Object(a.jsx)("div",{class:"col-md-12",children:Object(a.jsxs)("div",{class:"banner-caption",children:[Object(a.jsxs)("h4",{children:["Hello, this is ",Object(a.jsx)("em",{children:"Unistats"})," resource."]}),Object(a.jsx)("span",{children:"Statistics for Universities & Students & Enrollees"}),Object(a.jsxs)("p",{children:["Information and responses about lecturers and universities in ",Object(a.jsx)("strong",{children:"Ukraine"})]}),Object(a.jsx)("div",{class:"primary-button",children:Object(a.jsx)("a",{href:"/universities",children:"Proceed"})})]})})})})})})})}),Object(a.jsx)("section",{class:"services",children:Object(a.jsx)("div",{class:"container-fluid",children:Object(a.jsxs)("div",{class:"row",children:[Object(a.jsx)("div",{class:"col-md-4",children:Object(a.jsxs)("div",{class:"service-item fourth-item ",children:[Object(a.jsx)("div",{class:"icon"}),Object(a.jsx)("h4",{children:"Front-end"}),Object(a.jsxs)("p",{children:["Technologies: ",Object(a.jsx)("strong",{children:"React"}),", ",Object(a.jsx)("strong",{children:"Bootstrap"}),", ",Object(a.jsx)("strong",{children:"JQuery"}),", ",Object(a.jsx)("strong",{children:"HTML"}),", ",Object(a.jsx)("strong",{children:"CSS"}),", ",Object(a.jsx)("strong",{children:"JavaScript"})]})]})}),Object(a.jsx)("div",{class:"col-md-4",children:Object(a.jsxs)("div",{class:"service-item first-item ",children:[Object(a.jsx)("div",{class:"icon"}),Object(a.jsx)("h4",{children:"Back-end"}),Object(a.jsxs)("p",{children:["Technologies: ",Object(a.jsx)("strong",{children:"Python"}),", ",Object(a.jsx)("strong",{children:"Flask"}),", ",Object(a.jsx)("strong",{children:"PostgreSQL"})]})]})}),Object(a.jsx)("div",{class:"col-md-4",children:Object(a.jsxs)("div",{class:"service-item third-item",children:[Object(a.jsx)("div",{class:"icon"}),Object(a.jsx)("h4",{children:"Data Visualization"}),Object(a.jsxs)("p",{children:["Technologies: ",Object(a.jsx)("strong",{children:"MatPlotLib"}),", ",Object(a.jsx)("strong",{children:"Dash"})]})]})})]})})}),Object(a.jsx)("section",{class:"left-image",children:Object(a.jsx)("div",{class:"container-fluid",children:Object(a.jsxs)("div",{class:"row",children:[Object(a.jsx)("div",{class:"col-md-6",children:Object(a.jsx)("iframe",{src:"/media/6",title:"university",width:"100%",height:"400px",padding:"0px",margin:"0px auto"})}),Object(a.jsx)("div",{class:"col-md-6",children:Object(a.jsxs)("div",{class:"right-content",children:[Object(a.jsx)("h4",{children:"University Stats"}),Object(a.jsx)("p",{children:"Many universities apply to be on our resource and give information about lecturers, faculties, etc.. In response, we provide relevant stats about position of specific university, its ranking and enrolee's rates. With data we provide, university will be able to increase number of enrolee's and ranking among other competitors."}),Object(a.jsx)("div",{class:"primary-button",children:Object(a.jsx)("a",{href:"/universities",children:"Check Out"})})]})})]})})}),Object(a.jsx)("section",{class:"right-image",children:Object(a.jsx)("div",{class:"container-fluid",children:Object(a.jsxs)("div",{class:"row",children:[Object(a.jsx)("div",{class:"col-md-6",children:Object(a.jsxs)("div",{class:"left-content",children:[Object(a.jsx)("h4",{children:"Lecturers Stats"}),Object(a.jsx)("p",{children:"Also we provide data about lecturer's themselves, we have many criterias which will be plotted in beautiful statistical image. Students, which have learnt from specific lecturer will be able to leave their rate and feedback of his work "}),Object(a.jsx)("div",{class:"primary-button",children:Object(a.jsx)("a",{href:"/lecturers",children:"Check Out"})})]})}),Object(a.jsx)("div",{class:"col-md-6",children:Object(a.jsx)("iframe",{src:"/media/6",title:"university",width:"100%",height:"400px",padding:"0px",margin:"0px auto"})})]})})})]})})},m=function(e){e.data;var t={name:"\u0417\u0430\u0454\u0446\u044c \u0410\u043d\u0430\u0442\u043e\u043b\u0456\u0439 \u041f\u0430\u0432\u043b\u043e\u0432\u0438\u0447",description:"\u0434\u043e\u043a\u0442\u043e\u0440 \u044e\u0440\u0438\u0434\u0438\u0447\u043d\u0438\u0445 \u043d\u0430\u0443\u043a, \u043f\u0440\u043e\u0444\u0435\u0441\u043e\u0440, \u0447\u043b\u0435\u043d-\u043a\u043e\u0440\u0435\u0441\u043f\u043e\u043d\u0434\u0435\u043d\u0442 \u041d\u0430\u0446\u0456\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0457 \u0430\u043a\u0430\u0434\u0435\u043c\u0456\u0457 \u043f\u0440\u0430\u0432\u043e\u0432\u0438\u0445 \u043d\u0430\u0443\u043a \u0423\u043a\u0440\u0430\u0457\u043d\u0438, \u0417\u0430\u0441\u043b\u0443\u0436\u0435\u043d\u0438\u0439 \u044e\u0440\u0438\u0441\u0442 \u0423\u043a\u0440\u0430\u0457\u043d\u0438.         \u041e\u0441\u043d\u043e\u0432\u043d\u0456 \u043d\u0430\u043f\u0440\u044f\u043c\u0438 \u043d\u0430\u0443\u043a\u043e\u0432\u0438\u0445 \u0434\u043e\u0441\u043b\u0456\u0434\u0436\u0435\u043d\u044c: \u0442\u0435\u043e\u0440\u0435\u0442\u0438\u043a\u043e-\u043f\u043e\u043d\u044f\u0442\u0456\u0439\u043d\u0435 \u043e\u0441\u043c\u0438\u0441\u043b\u0435\u043d\u043d\u044f \u043f\u0440\u0430\u0432\u0430, \u0432\u0438\u0432\u0447\u0435\u043d\u043d\u044f \u0439\u043e\u0433\u043e \u043f\u0440\u0438\u0440\u043e\u0434\u0438, \u043f\u0440\u043e\u0446\u0435\u0441\u0443 \u043f\u0440\u0430\u0432\u043e\u0442\u0432\u043e\u0440\u0435\u043d\u043d\u044f, \u0432\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u043d\u044f \u0441\u043f\u0456\u0432\u0432\u0456\u0434\u043d\u043e\u0448\u0435\u043d\u043d\u044f \u043f\u0440\u0430\u0432\u0430 \u0456 \u0437\u0430\u043a\u043e\u043d\u0443, \u0434\u043e\u0441\u043b\u0456\u0434\u0436\u0435\u043d\u043d\u044f \u0432\u0437\u0430\u0454\u043c\u043e\u0437\u0432\u2019\u044f\u0437\u043a\u0456\u0432 \u043f\u0440\u0430\u0432\u0430 \u0456 \u0434\u0435\u0440\u0436\u0430\u0432\u0438 \u0442\u0430 \u0440\u043e\u043b\u0456 \u043f\u0440\u0430\u0432\u0430 \u0432 \u0444\u043e\u0440\u043c\u0443\u0432\u0430\u043d\u043d\u0456 \u0456 \u0444\u0443\u043d\u043a\u0446\u0456\u043e\u043d\u0443\u0432\u0430\u043d\u043d\u0456         \u0434\u0435\u0440\u0436\u0430\u0432\u0438 \u0456 \u0441\u0443\u0441\u043f\u0456\u043b\u044c\u0441\u0442\u0432\u0430; \u0442\u0435\u043e\u0440\u0435\u0442\u0438\u043a\u043e-\u043f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0456 \u0430\u0441\u043f\u0435\u043a\u0442\u0438  \u0444\u043e\u0440\u043c\u0443\u0432\u0430\u043d\u043d\u044f \u043f\u0440\u0430\u0432\u043e\u0432\u043e\u0457 \u0456 \u0441\u043e\u0446\u0456\u0430\u043b\u044c\u043d\u043e\u0457 \u0434\u0435\u0440\u0436\u0430\u0432\u0438 \u0442\u0430 \u0432\u0435\u0440\u0445\u043e\u0432\u0435\u043d\u0441\u0442\u0432\u0430 \u043f\u0440\u0430\u0432\u0430 \u0432 \u0423\u043a\u0440\u0430\u0457\u043d\u0456, \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0438 \u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u043d\u044f \u0443\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u043e\u0433\u043e \u043f\u0430\u0440\u043b\u0430\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0437\u043c\u0443, \u043e\u0440\u0433\u0430\u043d\u0456\u0437\u0430\u0446\u0456\u044f \u0442\u0430 \u0434\u0456\u044f\u043b\u044c\u043d\u0456\u0441\u0442\u044c \u043c\u0456\u0441\u0446\u0435\u0432\u043e\u0433\u043e \u0441\u0430\u043c\u043e\u0432\u0440\u044f\u0434\u0443\u0432\u0430\u043d\u043d\u044f, \u0434\u043e\u0441\u043b\u0456\u0434\u0436\u0435\u043d\u043d\u044f \u0444\u043e\u0440\u043c\u0438 \u043f\u0440\u0430\u0432\u043b\u0456\u043d\u043d\u044f,         \u0437\u0434\u0456\u0439\u0441\u043d\u0435\u043d\u043d\u044f \u043f\u0440\u0438\u043d\u0446\u0438\u043f\u0443 \u043f\u043e\u0434\u0456\u043b\u0443 \u0432\u043b\u0430\u0434\u0438; \u043a\u043e\u043d\u0441\u0442\u0438\u0442\u0443\u0446\u0456\u0439\u043d\u0435 \u0440\u0435\u0433\u0443\u043b\u044e\u0432\u0430\u043d\u043d\u044f \u0442\u0430 \u043c\u0435\u0445\u0430\u043d\u0456\u0437\u043c\u0438 \u0437\u0430\u0445\u0438\u0441\u0442\u0443 \u043f\u0440\u0430\u0432 \u0456 \u0441\u0432\u043e\u0431\u043e\u0434 \u043b\u044e\u0434\u0438\u043d\u0438 \u0456 \u0433\u0440\u043e\u043c\u0430\u0434\u044f\u043d\u0438\u043d\u0430.",position:"\u0437\u0430\u0432\u0456\u0434\u0443\u0432\u0430\u0447 \u043a\u0430\u0444\u0435\u0434\u0440\u0438 \u0437\u0430\u0433\u0430\u043b\u044c\u043d\u043e\u0442\u0435\u043e\u0440\u0435\u0442\u0438\u0447\u043d\u043e\u0433\u043e \u043f\u0440\u0430\u0432\u043e\u0437\u043d\u0430\u0432\u0441\u0442\u0432\u0430 \u0442\u0430 \u043f\u0443\u0431\u043b\u0456\u0447\u043d\u043e\u0433\u043e \u043f\u0440\u0430\u0432\u0430",courses:["\u041f\u0440\u0430\u0432\u043e \u0443 \u0432\u0440\u044f\u0434\u0443\u0432\u0430\u043d\u043d\u0456","\u041c\u0435\u0442\u043e\u0434\u043e\u043b\u043e\u0433\u0456\u044f \u043f\u0440\u0430\u0432\u043e\u0437\u043d\u0430\u0432\u0441\u0442\u0432\u0430","\u041f\u0440\u0430\u0432\u0430 \u043b\u044e\u0434\u0438\u043d\u0438 \u0442\u0430 \u0457\u0445 \u0437\u0430\u0445\u0438\u0441\u0442"],url_photo:"https://law.ukma.edu.ua/wp-content/uploads/2018/12/Zaiets.jpg",url_page:"https://law.ukma.edu.ua/specialists/zayets-anatolij-pavlovych/"},c=Object(l.f)();return console.log(c),console.log("/lecturersurvey_"+c.id),Object(a.jsxs)("div",{className:"lecturer",children:[Object(a.jsx)("section",{class:"left-image",children:Object(a.jsx)("div",{class:"container-fluid",children:Object(a.jsxs)("div",{class:"row",children:[Object(a.jsx)("div",{class:"col-md-6",children:Object(a.jsx)("img",{src:t.url_photo,alt:""})}),Object(a.jsx)("div",{class:"col-md-6",children:Object(a.jsxs)("div",{class:"right-content",style:{"margin-top":"40px"},children:[Object(a.jsx)("h4",{children:t.name}),Object(a.jsx)("h5",{children:t.position}),Object(a.jsx)("p",{children:t.description}),Object(a.jsx)("div",{style:{margin:"20px",width:"100%",float:"left"},className:"courses",children:t.courses.map((function(e){return Object(a.jsx)("div",{className:"filled-icon-button",style:{margin:"20px",width:"40%",float:"left"},children:Object(a.jsx)("a",{children:e})})}))}),Object(a.jsx)("div",{className:"primary-button",children:Object(a.jsx)("a",{href:t.url_page,style:{margin:"10px"},children:" Original Page "})})]})})]})})}),Object(a.jsx)("section",{class:"top-image",children:Object(a.jsx)("div",{class:"container-fluid",children:Object(a.jsx)("div",{class:"row",children:Object(a.jsxs)("div",{class:"col-md-8",style:{margin:"50px auto"},children:[Object(a.jsx)("img",{src:"assets/images/top-image.jpg",alt:""}),Object(a.jsxs)("div",{class:"down-content",children:[Object(a.jsx)("h4",{children:"Stats"}),Object(a.jsx)("p",{children:"Waiting for stats....."})]})]})})})}),Object(a.jsx)("div",{className:"col-md-6",style:{margin:"0px auto"},children:Object(a.jsx)("div",{className:"filled-rectangle-button",children:Object(a.jsx)("a",{href:"/lecturersurvey_"+c.id,children:" Survey "})})})]})},p=function(e){var t=e.data;return console.log(JSON.parse(t)),Object(a.jsx)("div",{children:Object(a.jsx)("div",{className:"universities",children:Object(a.jsx)(h,{})})})},v=function(){var e=Object(s.useState)("inactive"),t=Object(o.a)(e,2),c=t[0],i=t[1],r=Object(s.useState)({left:"0px",top:"0px"}),n=Object(o.a)(r,2),l=n[0],j=n[1];return Object(a.jsxs)("div",{children:[Object(a.jsx)("p",{className:"toggle",style:l,onClick:function(e){"inactive"===c?(i(""),j({left:"400px","font-size":"70px"})):(i("inactive"),j({left:"0px","font-size":"50px"}))},children:"inactive"===c?"\u2630":"\xd7"}),Object(a.jsx)("div",{id:"sidebar",className:c,children:Object(a.jsxs)("div",{class:"inner",children:[Object(a.jsx)("section",{id:"search",class:"alt"}),Object(a.jsx)("nav",{id:"menu",children:Object(a.jsxs)("ul",{children:[Object(a.jsx)("li",{children:Object(a.jsx)("a",{href:"/",children:"Homepage"})}),Object(a.jsx)("li",{children:Object(a.jsx)("a",{href:"/universities",children:"Universities Stats"})}),Object(a.jsx)("li",{children:Object(a.jsx)("a",{href:"/lecturers",children:"Lecturers Stats"})}),Object(a.jsx)("li",{children:Object(a.jsx)("a",{href:"/login",children:"Login or Register"})}),Object(a.jsx)("li",{children:Object(a.jsx)("a",{href:"/profile",children:"Profile"})})]})}),Object(a.jsx)("footer",{id:"footer",children:Object(a.jsxs)("p",{class:"copyright",children:[Object(a.jsx)("strong",{children:"Created by: "}),Object(a.jsx)("br",{}),Object(a.jsx)("br",{}),Object(a.jsx)("strong",{children:"  Bohdan Mahometa  "}),Object(a.jsx)("br",{}),Object(a.jsx)("br",{}),Object(a.jsx)("strong",{children:"  Fedir Zhydok  "}),Object(a.jsx)("br",{}),Object(a.jsx)("br",{}),Object(a.jsx)("strong",{children:"  Yaroslav Brovchenko  "}),Object(a.jsx)("br",{}),Object(a.jsx)("br",{}),Object(a.jsx)("strong",{children:"  Viktor Povazhuk  "}),Object(a.jsx)("br",{}),Object(a.jsx)("br",{}),Object(a.jsx)("strong",{children:"  Nikita Ishchenko  "})]})})]})})]})},f=function(e){var t=e.data;return console.log(JSON.parse(t)),Object(a.jsx)("section",{className:"contact-form",style:{margin:"100px"},children:Object(a.jsx)("div",{className:"row specially-for-form",children:Object(a.jsx)("div",{className:"col-md-6",children:Object(a.jsxs)("form",{id:"contact",method:"post",children:[Object(a.jsx)("div",{className:"col-md-12",children:Object(a.jsx)("fieldset",{children:Object(a.jsx)("input",{name:"email",type:"email",id:"email",size:"30",placeholder:"Email",required:!0})})}),Object(a.jsx)("div",{className:"col-md-12",children:Object(a.jsx)("fieldset",{children:Object(a.jsx)("input",{name:"password",type:"password",placeholder:"Password...",required:!0})})}),Object(a.jsx)("div",{className:"col-md-12",children:Object(a.jsx)("fieldset",{children:Object(a.jsx)("button",{type:"submit",id:"form-submit",class:"button",children:"Login"})})}),Object(a.jsx)("div",{className:"col-md-12",style:{"margin-top":"20px"},children:Object(a.jsx)("div",{className:"border-rounded-button",style:{width:"20%",margin:"0px auto"},children:Object(a.jsx)("a",{href:"/registration",style:{"text-decoration":"none"},children:"Register"})})})]})})})})},g=function(e){e.data;var t=Object(l.f)();return Object(a.jsx)("div",{children:Object(a.jsx)("h2",{children:t.id})})},y=function(e){var t=e.index,c=e.criteria,s=[1+5*parseInt(t),2+5*parseInt(t),3+5*parseInt(t),4+5*parseInt(t),5+5*parseInt(t)];return console.log(t),Object(a.jsxs)("div",{className:"stars in_wrapper",children:[Object(a.jsx)("h2",{children:c}),Object(a.jsx)("div",{className:"wrapper",children:s.map((function(e){return Object(a.jsxs)("div",{children:[Object(a.jsx)("input",{type:"radio",id:"r"+e,value:6-e%5===6?1:6-e%5,name:c},e),Object(a.jsx)("label",{htmlFor:"r"+e,children:"\u2605"})]})}))})]})},w=function(){return Object(a.jsx)("div",{children:Object(a.jsxs)("form",{method:"post",children:[["General rate","Sufficiency rate","Relevance rate","Loyalty rate","Politeness rate","Material rate","Punctuality rate","Objectivity rate","Adaptation rate","Complexity rate"].map((function(e,t){return Object(a.jsx)(y,{index:t,criteria:e})})),Object(a.jsx)("button",{type:"Submit",style:{margin:"50px auto"},children:"Submit"})]})})},N=function(){return Object(a.jsx)("div",{children:Object(a.jsxs)("form",{method:"post",children:[["General rate","Sufficiency rate","Relevance rate","Loyalty rate","Politeness rate","Material rate","Punctuality rate","Objectivity rate","Adaptation rate","Complexity rate"].map((function(e,t){return Object(a.jsx)(y,{index:t,criteria:e})})),Object(a.jsx)("button",{type:"Submit",children:"Submit"})]})})},S=function(e){var t=e.data;return console.log(JSON.parse(t)),Object(a.jsx)("div",{})},k=function(){return Object(a.jsxs)("div",{style:{margin:"200px auto"},children:[Object(a.jsx)("h1",{style:{"font-size":"150px"},children:"Congratulations!"}),Object(a.jsx)("h1",{style:{"font-size":"100px"},children:"You have loggined successfully!"}),Object(a.jsx)("h1",{style:{"font-size":"100px"},children:Object(a.jsx)("a",{href:"/",children:"Main Page"})})]})},P=function(){return Object(a.jsxs)("div",{style:{margin:"200px auto"},children:[Object(a.jsx)("h1",{style:{"font-size":"150px"},children:"Sorry"}),Object(a.jsx)("h1",{style:{"font-size":"100px"},children:"Something has gone wrong"}),Object(a.jsx)("h1",{style:{"font-size":"100px"},children:Object(a.jsx)("a",{href:"/",children:"Main Page"})})]})};var C=function(e){var t=e.data;return Object(a.jsx)(n.a,{children:Object(a.jsx)("div",{className:"App",id:"wrapper",children:Object(a.jsxs)("div",{id:"main",children:[Object(a.jsx)(j,{}),Object(a.jsx)(v,{}),Object(a.jsxs)(l.c,{children:[Object(a.jsx)(l.a,{path:"/lecturer_:id",render:function(){return Object(a.jsx)(m,{data:t})}}),Object(a.jsx)(l.a,{path:"/university_:id",render:function(){return Object(a.jsx)(g,{data:t})}}),Object(a.jsx)(l.a,{path:"/survey_:id",render:function(){return Object(a.jsx)(N,{data:t})}}),Object(a.jsx)(l.a,{path:"/lecturersurvey_:id",render:function(){return Object(a.jsx)(w,{data:t})}}),Object(a.jsx)(l.a,{exact:!0,path:"/",children:Object(a.jsx)(u,{data:t})}),Object(a.jsx)(l.a,{exact:!0,path:"/surveys",children:Object(a.jsx)(S,{data:t})}),Object(a.jsx)(l.a,{exact:!0,path:"/registration",children:Object(a.jsx)(O,{data:t})}),Object(a.jsx)(l.a,{exact:!0,path:"/profile",children:Object(a.jsx)(x,{data:t})}),Object(a.jsx)(l.a,{exact:!0,path:"/universities",children:Object(a.jsx)(b,{data:t})}),Object(a.jsx)(l.a,{exact:!0,path:"/lecturers",children:Object(a.jsx)(p,{data:t})}),Object(a.jsx)(l.a,{exact:!0,path:"/login",children:Object(a.jsx)(f,{data:t})}),Object(a.jsx)(l.a,{exact:!0,path:"/surveys",children:Object(a.jsx)(S,{data:t})}),Object(a.jsx)(l.a,{exact:!0,path:"/success_login",children:Object(a.jsx)(k,{})}),Object(a.jsx)(l.a,{exact:!0,path:"/unsuccess_login",children:Object(a.jsx)(P,{})})]})]})})})};r.a.render(Object(a.jsx)(C,{data:window.token}),document.getElementById("root"))}},[[32,1,2]]]);
//# sourceMappingURL=main.8cdfc4a0.chunk.js.map