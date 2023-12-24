const endpoint = 'http://127.0.0.1:5000/get_groups';

fetch(endpoint, {
    method: 'GET',
   // mode: 'no-cors'
  })
  .then(response => response.json())
  .then(data => {
    //'data' = JSON data
    console.log(data);
    const groupsArray = Object.values(data).map(item => item.group);
    const uniqueGroups = [...new Set(groupsArray)];
    uniqueGroups.forEach(el => {
      let gr_option=document.createElement('option');
      gr_option.value=el;
      gr_option.className='group_option'
      gr_option.innerHTML=el
      gr_option.id= Object.keys(data).find(key => data[key].group === el);
      gr_selector.appendChild(gr_option)
    });
    console.log(uniqueGroups);
  })
  .catch(error => console.error('Error fetching data:', error));


const gr_selector=document.getElementById('group');


document.getElementById('pageForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var selectElement = document.getElementById("group");

    // Get the selected <option> element
    var selectedOption = selectElement.options[selectElement.selectedIndex]
    // Get the id attribute of the selected option
    var gr_ID = selectedOption.id;

    let gr_option=document.querySelector('#group').value;
    //let gr_ID=document.querySelector('#group').id;
    
    var selectedValue = document.getElementById('group').value;
      var redirectUrl = getRedirectUrl(selectedValue);
      window.location.href = redirectUrl + "?group="+ encodeURIComponent(gr_option)+"&groupID="+encodeURIComponent(gr_ID);
    });
    function getRedirectUrl(selectedValue) {
      switch (selectedValue) {
        case 'General':
          return 'general_schedule.html'; 
        default:
          //save the group for next page
          return 'group_schedule.html';
      }
    }