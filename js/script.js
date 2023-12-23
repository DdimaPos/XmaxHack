document.addEventListener('DOMContentLoaded', function () {
    fetch('../data/Profesori.csv')
        .then(response => response.text())
        .then(data => {
            // Parse CSV data
            const rows = data.split('\n');
            const headers = rows[0].split(',');

            // Create HTML table headers
            const table = document.getElementById('excelTable');
            const thead = document.createElement('thead');
            const headerRow = document.createElement('tr');

            headers.forEach(header => {
                const th = document.createElement('th');
                th.textContent = header;
                headerRow.appendChild(th);
            });

            thead.appendChild(headerRow);
            table.appendChild(thead);

            // Create HTML table body
            const tbody = document.createElement('tbody');
            rows.slice(1).forEach(row => {
                const rowData = row.split(',');
                const tr = document.createElement('tr');

                rowData.forEach(cellData => {
                    const td = document.createElement('td');
                    td.textContent = cellData;
                    tr.appendChild(td);
                });

                tbody.appendChild(tr);
            });

            table.appendChild(tbody);
        })
        .catch(error => console.error('Error fetching data:', error));
});
