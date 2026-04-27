function syncToMySQL() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Dados");
  var data = sheet.getDataRange().getValues(); // Pega tudo
  var header = data.shift(); // Remove o cabeçalho
  
  var payload = data.map(function(row) {
    return {
      "id": row[0],     // Coluna A
      "nome": row[1],   // Coluna B
      "status": row[2]  // Coluna C
    };
  }).filter(row => row.id !== ""); // Ignora linhas vazias

  var url = "http://SEU_IP_OU_NGROK/sync-batch";
  var options = {
    "method": "post",
    "contentType": "application/json",
    "payload": JSON.stringify(payload)
  };

  try {
    UrlFetchApp.fetch(url, options);
    console.log("Sincronização concluída.");
  } catch (e) {
    console.error("Falha na sincronização: " + e);
  }
}