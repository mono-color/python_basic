$(document).ready(function(){
    $(document).on('click', '#id_table tr', function(){
        searchAjax($(this).children().eq(2).text());
    });
    function searchAjax(coin){
    var subUrl = 'https://api.upbit.com/v1/ticker?markets=' + coin
    $.ajax({
        url : subUrl
        ,dataType : 'json'
        ,success : function(data){
            console.log(data)
            var keys = Object.keys(data[0]);
            console.log(keys)
            var str = "";
            for(var i = 0; i < keys.length; i++){
                str += "<tr>";
                str += "<td>" + keys[i] + "</td>";
                str += "<td>" + data[0][keys[i]] + "</td>";
                str += "</tr>";
            }
            document.getElementById('id_table_sub').innerHTML = str;
        }
        ,error(e){
        console.log(e)
        }
    })
    }
});