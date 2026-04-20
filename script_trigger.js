function onEdit(e) {
  var range = e.range;
  var sheet = range.getSheet();
  
  // Configurações: Apenas monitora a aba 'Dados'
  if (sheet.getName() !== "Dados") return;

  var idRegistro = sheet.getRange(range.getRow(), 1).getValue(); // Assume que ID está na coluna A
  var nomeColuna = sheet.getRange(1, range.getColumn()).getValue(); // Nome da coluna na linha 1
  var novoValor = range.getValue();

  var url = "https://hungry-easter-condiment.ngrok-free.dev/update-sheet"; // URL do ngrok que eu gerei no terminal
  
  var payload = {
    "id_registro": idRegistro,
    "coluna": nomeColuna,
    "novo_valor": String(novoValor)
  };

  var options = {
    "method": "post",
    "contentType": "application/json",
    "payload": JSON.stringify(payload),
    "muteHttpExceptions": true
  };

  UrlFetchApp.fetch(url, options);
}
