$(function(){
			$('.top2 div,.left div').click(function(){
				// 当前点击的按钮加上current样式后，除了当前，其他的按钮去掉current样式
				$(this).addClass('current').siblings().removeClass('current');
				//取变量
				var a = $(this).parent().attr('class'); //tab的类型
				var b = $(this).index(); //tab的id
				var data = {
					data: JSON.stringify({
						'tabType': a,
						'tabIndex': b
					})
				}
				//ajax 提交数据
				$.ajax({
					type: "POST",
					dataType: "json",
					url: "/merchant",//后端请求
					data: data,
					success: function (result) {
						$(".right").html(data);
					},
					error: function (result) {
						$(".right").html("获取数据失败！");
					}
				})
						})
			})

$(document).ready(function(){
    var searchKey = $(".input").val();
    if (undefined == searchKey) searchKey = "";
    var params = {
        searchKey:searchKey
    };
    //ajax 提交数据
    $.ajax({
        type: "GET",
        dataType: "json",
        url: url_for('apiBP.index')
        data: {'searchKey':searchKey},
        success: function (result) {
            $(".right").html(template("index/index_logined.html", {datas:result.data.datas}));
        },
        error: function (result) {
            $(".right").html("获取数据失败！");
        }
    })
}