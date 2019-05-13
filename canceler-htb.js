cancelled = []

function check(){
 $('#shouts > p').each((index) => {
  let mssg = $('#shouts > p:nth-child('+index+')').text()
  if (mssg.includes("requested a reset on Netmon")) {
   let le_cancel = mssg.match(/cancel \d\d\d\d\d\d/);
   if (!(cancelled.includes(le_cancel))) {
    $('#container-text-shout > div > div.emojionearea-editor').text('/' + le_cancel[0]);
    $('body > div.wrapper > section > div > div.panel > div.panel-footer > div > div.col-xs-1 > button')[0].click();
    cancelled.push(le_cancel)
   }
        }
 })
 setTimeout(check, 5000)
}
