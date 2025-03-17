import java.awt.Desktop;
import java.io.File;
import java.io.IOException;
import com.itextpdf.layout.element.Table;
import com.itextpdf.layout.element.Cell;
import com.itextpdf.layout.element.Paragraph;
import com.itextpdf.layout.element.Spacer;
import com.itextpdf.layout.property.TextAlignment;
import com.itextpdf.layout.property.VerticalAlignment;
import com.itextpdf.kernel.colors.ColorConstants;
import com.itextpdf.kernel.pdf.PdfDocument;
import com.itextpdf.kernel.pdf.PdfWriter;
import com.itextpdf.layout.Document;

public class CalibrationCertificate {

    public static void main(String[] args) {
        String filePath = "calibration_certificate.pdf";

        try {
            // Create PDF writer and document
            PdfWriter writer = new PdfWriter(filePath);
            PdfDocument pdf = new PdfDocument(writer);
            Document document = new Document(pdf);

            // Title
            Paragraph title = new Paragraph("Certificado de Calibração")
                    .setTextAlignment(TextAlignment.CENTER)
                    .setFontSize(18)
                    .setBold();
            document.add(title);

            // Spacer
            document.add(new Spacer(1, 10));

            // Subtitle
            Paragraph subtitle = new Paragraph("Serviço nº: CACV215/24")
                    .setTextAlignment(TextAlignment.CENTER)
                    .setFontSize(12)
                    .setBold();
            document.add(subtitle);

            // Spacer
            document.add(new Spacer(1, 20));

            // Table data
            String[][] data = {
                    {"Frequência de análise", "Valor de referência", "Valor do equipamento", "Erro", "Incerteza expandida"},
                    {"1000 Hz", "92.0 dB SPL", "92.0 dB SPL", "0.0 dB", "± 0.12 dB"},
                    {"63 Hz", "91.9 dB SPL", "91.8 dB SPL", "-0.1 dB", "± 0.12 dB"},
                    {"125 Hz", "91.9 dB SPL", "91.8 dB SPL", "-0.2 dB", "± 0.12 dB"},
                    {"250 Hz", "91.9 dB SPL", "91.8 dB SPL", "-0.1 dB", "± 0.12 dB"},
                    {"500 Hz", "92.0 dB SPL", "91.9 dB SPL", "-0.1 dB", "± 0.12 dB"},
                    {"1000 Hz", "92.0 dB SPL", "91.8 dB SPL", "-0.2 dB", "± 0.12 dB"},
                    {"2000 Hz", "92.0 dB SPL", "91.8 dB SPL", "-0.2 dB", "± 0.12 dB"},
                    {"4000 Hz", "92.0 dB SPL", "91.7 dB SPL", "-0.3 dB", "± 0.12 dB"},
                    {"8000 Hz", "92.0 dB SPL", "91.6 dB SPL", "-0.4 dB", "± 0.12 dB"},
                    {"16000 Hz", "92.0 dB SPL", "86.7 dB SPL", "-5.3 dB", "± 0.12 dB"},
            };

            // Create table
            Table table = new Table(data[0].length);
            for (int row = 0; row < data.length; row++) {
                for (int col = 0; col < data[row].length; col++) {
                    Cell cell = new Cell().add(new Paragraph(data[row][col]));
                    if (row == 0) {
                        // Header row styling
                        cell.setBackgroundColor(ColorConstants.LIGHT_GRAY);
                        cell.setBold();
                        cell.setTextAlignment(TextAlignment.CENTER);
                        cell.setVerticalAlignment(VerticalAlignment.MIDDLE);
                    } else {
                        // Data row styling
                        cell.setTextAlignment(TextAlignment.CENTER);
                        cell.setVerticalAlignment(VerticalAlignment.MIDDLE);
                    }
                    table.addCell(cell);
                }
            }

            // Add table to document
            document.add(table);

            // Close document
            document.close();

            // Open PDF file
            File file = new File(filePath);
            if (Desktop.isDesktopSupported()) {
                Desktop.getDesktop().open(file);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}