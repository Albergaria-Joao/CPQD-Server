function syncToMySQL() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Dados");
  var data = sheet.getDataRange().getValues(); // Pega tudo
  var header = data.shift(); // Remove o cabeçalho

  var payload = data.map(function (row) {
    return {
      "nome": row[0],
      "modelo": row[1],
      "marca": row[2],
      "cor": row[3],
      "placa": String(row[4]).toUpperCase().trim(),
      "empresa": row[5],
    };
  }).filter(row => row.placa !== "" && row.nome !== ""); // Ignora linhas vazias

  var url = "https://hungry-easter-condiment.ngrok-free.dev/sync-sheet";
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