(function(){var t={8904:function(t,e,n){"use strict";var o=n(9242),r=n(3396);function i(t,e){const n=(0,r.up)("router-view");return(0,r.wg)(),(0,r.j4)(n)}var a=n(89);const s={},u=(0,a.Z)(s,[["render",i]]);var c=u,l=n(2483);const d={class:"home"};function f(t,e,n,o,i,a){const s=(0,r.up)("Art");return(0,r.wg)(),(0,r.iD)("div",d,[(0,r.Wm)(s,{image:"park.jpg"})])}var p=n(7139);const g={class:"container"},h={class:"vl-parent"},m=["src"];function v(t,e,o,i,a,s){const u=(0,r.up)("loading");return(0,r.wg)(),(0,r.iD)("div",g,[(0,r._)("div",h,[(0,r.Wm)(u,{active:a.loading,"onUpdate:active":e[0]||(e[0]=t=>a.loading=t),"is-full-page":!0},null,8,["active"])]),(0,r._)("img",{class:"image-container",style:(0,p.j5)([a.music_started?{opacity:1}:{opacity:.6}]),ref:"art",src:n(7173)(`./${o.image}`),onMousemove:e[1]||(e[1]=(...t)=>s.updateNote&&s.updateNote(...t))},null,44,m),a.music_started?(0,r.kq)("",!0):((0,r.wg)(),(0,r.iD)("button",{key:0,class:"btn",onClick:e[2]||(e[2]=(...t)=>s.start&&s.start(...t))}," Start "))])}var b=n(5513),y=n.n(b),_=n(4311),w=n(1657);const k="https://backend.interactiveart.web.illinois.edu";var j={name:"Art",components:{Loading:y()},props:{image:String},data(){return{notes:void 0,loading:!1,music_started:!1,time_delay:800,base_url:""}},created(){window.addEventListener("load",(()=>{this.image_height=this.$refs.art.clientHeight,this.image_width=this.$refs.art.clientWidth})),location.toString().includes("localhost")||(this.base_url=k)},methods:{load_notes_audio(){var t=`${this.base_url}/coords/${this.image}/${this.image_width}/${this.image_height}`;console.log(`getting notes from backend at ${t}`),_.Z.get(t).then((t=>{this.notes=t.data.notes,console.log("notes loaded from backend")})).catch((t=>{console.log(`failed getting notes from backend: ${t}`)})).finally((()=>{console.log(`note array num rows: ${this.notes.length}, cols: ${this.notes[0].length}`),this.synth=new w.Z({onload:()=>{console.log("audio samples loaded"),this.loading=!1,this.music_started=!0}}).toDestination()}))},updateNote(t){if(this.music_started&&!this.loading&&(!this.start_time||new Date-this.start_time>this.time_delay)){var e=t.offsetX,n=t.offsetY,o=this.notes[e][n];this.synth.triggerAttack(o),console.log(`note playing: ${o} for x: ${e}, y: ${n}`),this.start_time=new Date}},start(){this.loading=!0,this.load_notes_audio()}}};const O=(0,a.Z)(j,[["render",v],["__scopeId","data-v-b9bd29c4"]]);var $=O,x={name:"HomeView",components:{Art:$}};const E=(0,a.Z)(x,[["render",f]]);var A=E;const C=[{path:"/",name:"home",component:A},{path:"/about",name:"about",component:()=>n.e(443).then(n.bind(n,7381))}],D=(0,l.p7)({history:(0,l.PO)("/"),routes:C});var N=D;(0,o.ri)(c).use(N).mount("#app")},7173:function(t,e,n){var o={"./joy.jpg":4032,"./park.jpg":7078,"./test-art.jpg":5456};function r(t){var e=i(t);return n(e)}function i(t){if(!n.o(o,t)){var e=new Error("Cannot find module '"+t+"'");throw e.code="MODULE_NOT_FOUND",e}return o[t]}r.keys=function(){return Object.keys(o)},r.resolve=i,t.exports=r,r.id=7173},4032:function(t,e,n){"use strict";t.exports=n.p+"img/joy.7223429a.jpg"},7078:function(t,e,n){"use strict";t.exports=n.p+"img/park.898a205c.jpg"},5456:function(t,e,n){"use strict";t.exports=n.p+"img/test-art.99bb4658.jpg"}},e={};function n(o){var r=e[o];if(void 0!==r)return r.exports;var i=e[o]={exports:{}};return t[o].call(i.exports,i,i.exports,n),i.exports}n.m=t,function(){var t=[];n.O=function(e,o,r,i){if(!o){var a=1/0;for(l=0;l<t.length;l++){o=t[l][0],r=t[l][1],i=t[l][2];for(var s=!0,u=0;u<o.length;u++)(!1&i||a>=i)&&Object.keys(n.O).every((function(t){return n.O[t](o[u])}))?o.splice(u--,1):(s=!1,i<a&&(a=i));if(s){t.splice(l--,1);var c=r();void 0!==c&&(e=c)}}return e}i=i||0;for(var l=t.length;l>0&&t[l-1][2]>i;l--)t[l]=t[l-1];t[l]=[o,r,i]}}(),function(){n.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return n.d(e,{a:e}),e}}(),function(){n.d=function(t,e){for(var o in e)n.o(e,o)&&!n.o(t,o)&&Object.defineProperty(t,o,{enumerable:!0,get:e[o]})}}(),function(){n.f={},n.e=function(t){return Promise.all(Object.keys(n.f).reduce((function(e,o){return n.f[o](t,e),e}),[]))}}(),function(){n.u=function(t){return"js/about.3006b34b.js"}}(),function(){n.miniCssF=function(t){}}(),function(){n.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(t){if("object"===typeof window)return window}}()}(),function(){n.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)}}(),function(){var t={},e="interactive-art-ui:";n.l=function(o,r,i,a){if(t[o])t[o].push(r);else{var s,u;if(void 0!==i)for(var c=document.getElementsByTagName("script"),l=0;l<c.length;l++){var d=c[l];if(d.getAttribute("src")==o||d.getAttribute("data-webpack")==e+i){s=d;break}}s||(u=!0,s=document.createElement("script"),s.charset="utf-8",s.timeout=120,n.nc&&s.setAttribute("nonce",n.nc),s.setAttribute("data-webpack",e+i),s.src=o),t[o]=[r];var f=function(e,n){s.onerror=s.onload=null,clearTimeout(p);var r=t[o];if(delete t[o],s.parentNode&&s.parentNode.removeChild(s),r&&r.forEach((function(t){return t(n)})),e)return e(n)},p=setTimeout(f.bind(null,void 0,{type:"timeout",target:s}),12e4);s.onerror=f.bind(null,s.onerror),s.onload=f.bind(null,s.onload),u&&document.head.appendChild(s)}}}(),function(){n.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})}}(),function(){n.p="/"}(),function(){var t={143:0};n.f.j=function(e,o){var r=n.o(t,e)?t[e]:void 0;if(0!==r)if(r)o.push(r[2]);else{var i=new Promise((function(n,o){r=t[e]=[n,o]}));o.push(r[2]=i);var a=n.p+n.u(e),s=new Error,u=function(o){if(n.o(t,e)&&(r=t[e],0!==r&&(t[e]=void 0),r)){var i=o&&("load"===o.type?"missing":o.type),a=o&&o.target&&o.target.src;s.message="Loading chunk "+e+" failed.\n("+i+": "+a+")",s.name="ChunkLoadError",s.type=i,s.request=a,r[1](s)}};n.l(a,u,"chunk-"+e,e)}},n.O.j=function(e){return 0===t[e]};var e=function(e,o){var r,i,a=o[0],s=o[1],u=o[2],c=0;if(a.some((function(e){return 0!==t[e]}))){for(r in s)n.o(s,r)&&(n.m[r]=s[r]);if(u)var l=u(n)}for(e&&e(o);c<a.length;c++)i=a[c],n.o(t,i)&&t[i]&&t[i][0](),t[i]=0;return n.O(l)},o=self["webpackChunkinteractive_art_ui"]=self["webpackChunkinteractive_art_ui"]||[];o.forEach(e.bind(null,0)),o.push=e.bind(null,o.push.bind(o))}();var o=n.O(void 0,[998],(function(){return n(8904)}));o=n.O(o)})();
//# sourceMappingURL=app.337a55fa.js.map