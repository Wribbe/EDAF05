import java.util.*;
import java.nio.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.charset.Charset;
import java.io.*;

class Compare {
    public static void main(String[] args) {
        String filename1 = args[0];
        String filename2 = args[1];

        List<String> lines1 = new ArrayList<String>();
        List<String> lines2 = new ArrayList<String>();
        boolean mismatch = false;
            try {
                lines1 = Files.readAllLines(Paths.get(filename1), Charset.defaultCharset());
                lines2 = Files.readAllLines(Paths.get(filename2), Charset.defaultCharset());
            } catch (IOException e) {
                e.printStackTrace();
            }
        for(int i=0; i<lines1.size(); i++) {
            if (lines1.get(i).equals(lines2.get(i))) {
                continue;
            } else {
                System.out.println(String.format("%s does not equal %s!",
                                                 filename1,
                                                 filename2));
                System.out.println(String.format("Mismatch in following line: %s != %s", lines1.get(i), lines2.get(i)));
                mismatch = true;
                break;
            }
        }
        if (!mismatch) {
            System.out.println(String.format("%s equals %s!", filename1,
                                                              filename2));
        }
    }
}
