
  <script>
      let humberger = document.querySelector(".hamburger .fas");
      let closeBtn = document.querySelector(".close");


      humberger.addEventListener("click", function(){
        let wrapper = document.querySelector(".wrapper");
        wrapper.classList.add("active");
      });

      closeBtn.addEventListener("click",function(){
        let wrapper = document.querySelector(".wrapper");
       wrapper.classList.remove("active");
      })
    </script>
