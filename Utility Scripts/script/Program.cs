using System;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using OfficeOpenXml;
using OfficeOpenXml.Style;

class Program
{
    static void Main(string[] args)
    {
        string connectionString = "Server=localhost;Database=Test;Trusted_Connection=True;";

        using (SqlConnection connection = new SqlConnection(connectionString))
        {
            connection.Open();

            // Get table information
            DataTable tables = connection.GetSchema("Tables");
            using (ExcelPackage excelPackage = new ExcelPackage())
            {
                ExcelWorksheet worksheet = excelPackage.Workbook.Worksheets.Add("columns");
                int rowInExcel = 1;
                foreach (DataRow tableRow in tables.Rows)
                {
                    string? tableName = tableRow["TABLE_NAME"].ToString();
                    worksheet.Cells[rowInExcel, 1].Value = tableName;
                    worksheet.Cells[rowInExcel, 1].Style.Font.Bold = true;
                    rowInExcel += 1;
                    DecorateCell(worksheet, "Column", rowInExcel, 1);
                    DecorateCell(worksheet, "Existing Type", rowInExcel, 2);
                    DecorateCell(worksheet, "Size of existing type", rowInExcel, 3);
                    DecorateCell(worksheet, "Max Len of data", rowInExcel, 4);
                    rowInExcel += 1;

                    // Get the column information for each table
                    DataTable columns = connection.GetSchema("Columns", new[] { null, null, tableName });

                    foreach (DataRow columnRow in columns.Rows)
                    {
                        string? columnName = columnRow["COLUMN_NAME"].ToString();
                        string? dataType = columnRow["DATA_TYPE"].ToString();
                        string? size = string.IsNullOrEmpty(columnRow["CHARACTER_MAXIMUM_LENGTH"].ToString()) ? "NULL" : columnRow["CHARACTER_MAXIMUM_LENGTH"].ToString();

                        string query = $"SELECT MAX(LEN([{columnName}])) FROM [{tableName}]";
                        using (SqlCommand command = new SqlCommand(query, connection))
                        {
                            string? maxLength = command.ExecuteScalar().ToString();
                            worksheet.Cells[rowInExcel, 1].Value = columnName;
                            worksheet.Cells[rowInExcel, 2].Value = dataType;
                            worksheet.Cells[rowInExcel, 3].Value = size;
                            worksheet.Cells[rowInExcel, 4].Value = maxLength;

                            rowInExcel++;
                        }
                    }
                    
                    rowInExcel++;
                }
                excelPackage.SaveAs(new System.IO.FileInfo("TableColumns.xlsx"));
            }
            
        }

        

        Console.WriteLine("Table and column information exported to Excel successfully!");
    }

    private static void DecorateCell(ExcelWorksheet worksheet, string name, int x, int y)
    {   
        worksheet.Cells[x, y].Value = name;
        worksheet.Cells[x, y].Style.Font.Bold = true;
        worksheet.Cells[x, y].Style.WrapText = true;
        worksheet.Cells[x, y].Style.Border.BorderAround(ExcelBorderStyle.Thin);
        worksheet.Cells[x, y].Style.Fill.PatternType = ExcelFillStyle.Solid;
        worksheet.Cells[x, y].Style.Fill.BackgroundColor.SetColor(Color.FromArgb(255, 180, 198, 231));
    }
}
