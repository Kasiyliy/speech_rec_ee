package kz.halyqteam.servlet;

import kz.halyqteam.service.RecognizeService;

import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;
import java.io.IOException;
import java.io.PrintWriter;

/**
 * @author Assylkhan
 * on 28.01.2019
 * @project speech_rec_ee
 */
@WebServlet(urlPatterns = "/api/uploadFile")
@MultipartConfig
public class SpeechRec extends HttpServlet{
    private static String MIME_TYPE = "audio/wave";

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String res = "";
        resp.setCharacterEncoding("UTF-8");
        resp.setContentType("application/json");
        Part filePart = req.getPart("file");
        String files = filePart.getContentType();
        if(!files.equals(MIME_TYPE)){
            res  =   "{ \"message\" : \"mime type error\" , \"error\" : true  }";
        }

        PrintWriter out = resp.getWriter();

        if(res.length() == 0){
            RecognizeService recognizeService = new RecognizeService();

            try{
                res = recognizeService.recognize(filePart.getInputStream());
            }catch (Exception e){
                e.printStackTrace();
                res  = "{\"message\" : \"not recognized\"  ,\"error\" : true }";
            }
        }

        out.print(res);

    }
}
