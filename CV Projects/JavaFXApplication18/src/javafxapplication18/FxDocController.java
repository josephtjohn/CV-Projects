/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javafxapplication18;
import java.net.URL;
import java.util.ResourceBundle; import javafx.event.ActionEvent; import
javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.control.Button; import javafx.scene.control.Label; import
javafx.scene.control.RadioButton; import javafx.scene.control.TextField; import
javafx.scene.control.ToggleGroup;
import javafx.stage.Stage;
/**
*
*
*/
public class FxDocController implements Initializable {
 @FXML
 private Label label;
 @FXML
 private void handleButtonAction(ActionEvent event) {
 System.out.println("You clicked me!");
 label.setText("Hello World!");
 }
 @Override
 public void initialize(URL url, ResourceBundle rb) {
// TODO
 }
 @FXML
 private Button gpa;
 @FXML
 private Button show;
 @FXML
 private Button exit;
 @FXML
 private RadioButton r1;
 @FXML
 private RadioButton r2;
 @FXML
 private TextField t2;
 @FXML
 private TextField t3;
 @FXML
 private TextField t4;
 @FXML
 private TextField t5;
 @FXML
 private TextField t6;
 @FXML
 private TextField t1;
 @FXML
 private TextField t7;
 @FXML
 private TextField t8;
 @FXML
 private TextField t9;
 public void GPA(int m1, int m2, int m3, int m4, int m5, int m6) {
 float total = m1 + m2 + m3 + m4 + m5 + m6;
 float avg = total / 6;
 t8.setText(Float.toString(total));
 t9.setText(Float.toString(avg));
 }
 public void GPA1(int m1, int m2, int m3, int m4) {
 float total = m1 + m2 + m3 + m4;
 float avg = total / 4;
 t8.setText(Float.toString(total));
 t9.setText(Float.toString(avg));
 }
 @FXML
 private void handleButtonAction_gpa(ActionEvent event) {
 ToggleGroup member = new ToggleGroup();
 r1.setToggleGroup(member);
 r2.setToggleGroup(member);
 RadioButton rb = (RadioButton) member.getSelectedToggle();
 String choice = rb.getText();
 if (choice.equals("MCA")) {
 int m1 = Integer.parseInt(t2.getText());
 int m2 = Integer.parseInt(t3.getText());
 int m3 = Integer.parseInt(t4.getText());
 int m4 = Integer.parseInt(t5.getText());
 int m5 = Integer.parseInt(t6.getText());
 int m6 = Integer.parseInt(t7.getText());
 GPA(m1, m2, m3, m4, m5, m6);
 } else {
 r2.setSelected(false);
 int m1 = Integer.parseInt(t2.getText());
 int m2 = Integer.parseInt(t2.getText());
 int m3 = Integer.parseInt(t2.getText());
 int m4 = Integer.parseInt(t2.getText());
 GPA1(m1, m2, m3, m4);
 }
 }
 @FXML
 private void handleButtonAction_show(ActionEvent event) {
 }
 @FXML
 private void handleButtonAction_exit(ActionEvent event) {
 }
 @FXML
 public void handleCloseButtonAction(ActionEvent event) {
 Stage stage = (Stage) exit.getScene().getWindow();
 stage.close();
 }
 private void isClicked(ActionEvent event) {
 Node year3_1 = null;
 if (r2.isSelected()) {
 t6.setDisable(true);
 } else {
 t6.setDisable(false);
 }
 }
}
