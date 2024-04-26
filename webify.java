//import needed classes from respective packages
import java.net.URL;
import java.util.*;
import java.io.*;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

class htmlconverter {

    //create a method that identifies patterns in text that can convert to HTML links
    public static String converter(String line) {
        

        if (line.length() != 0) {

            String patternString = "\\[\\[([a-zA-Z]+)\\]\\[([a-zA-Z]+)\\]\\]";
            Pattern r = Pattern.compile(patternString);
            Matcher s = r.matcher(line);

            if (s.find()) {
                String x = s.group(1);
                String y = s.group(2);
                String link = "<a href=" + x + ">" + y + "</a>";
                System.out.println(s.group(0));
                line = s.replaceAll(link);
            }
            if (line.charAt(0) == '_' && line.charAt(line.length() - 1) == '_') {
                return "<h1>" + line.substring(1, line.length() - 1) + "</h1>";
            }

            if (line.charAt(0) == '-') {
                return "<li>" + line.substring(1, line.length()) + "</li>";
            } 
            else {
              return line + "<br>";
            }
        } 
        else {
          return "<br><p></p>";
        }
    }

    //main method that prompts the user for input and executes the function
    //the user inputs a file with is converted to a new copy of said file in HTML

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        System.out.println("Choose a file to convert: ");
        String filename = scan.nextLine();
        int dotPosition = filename.lastIndexOf(".");
        String outputfilename = filename.substring(0, dotPosition) + ".html";

        URL path = ClassLoader.getSystemResource(filename);
        File file = new File(path.getFile());
        
        try {
            BufferedReader br = new BufferedReader(new FileReader(file));

            StringBuilder html = new StringBuilder();
            html.append("<html> <body>");
            
            String st;
            while ((st = br.readLine()) != null) {
                html.append(converter(st));
                
            }
            html.append("</body> </html>");
            System.out.println(html);

            file = new File(outputfilename);
            if (file.createNewFile()) {
                System.out.println("File is created!");
            } else {
                System.out.println("File already exists.");
            }

            FileWriter writer = new FileWriter(file);
            writer.write(html.toString());
            writer.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
