/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javafxapplication18;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.layout.BorderPane;
public class JavaFXApplication18 extends Application {
 public void start(Stage primaryStage) {
 try {
 Parent root = FXMLLoader.load(getClass().getResource("FxDoc.fxml"));
 Scene scene = new Scene(root);
 primaryStage.setScene(scene);
 primaryStage.show();
 } catch (Exception e) {
 e.printStackTrace();
 }
 }
 public static void main(String[] args) {
 launch(args);
 }
}
<?xml version="1.0" encoding="UTF-8"?>
<?import javafx.geometry.Insets?>
<?import javafx.scene.control.Button?>
<?import javafx.scene.control.Label?>
<?import javafx.scene.control.RadioButton?>
<?import javafx.scene.control.TableColumn?>
<?import javafx.scene.control.TableView?>
<?import javafx.scene.control.TextField?>
<?import javafx.scene.layout.AnchorPane?>
<?import javafx.scene.layout.HBox?>
<AnchorPane id="AnchorPane" prefHeight="560.0" prefWidth="530.0"
xmlns="http://javafx.com/javafx/17" xmlns:fx="http://javafx.com/fxml/1"
fx:controller="application.FxDocController">
<children>
<HBox layoutX="89.0" layoutY="54.0" prefHeight="26.0" prefWidth="400.0" style="-fxborder-color: black;" />
<Button fx:id="gpa" layoutX="397.0" layoutY="100.0"
onAction="#handleButtonAction_gpa" text="GPA" />
<Label fx:id="label" layoutX="126" layoutY="120" minHeight="16" minWidth="69" />
<Button fx:id="show" layoutX="397.0" layoutY="137.0"
onAction="#handleButtonAction_show" text="REPORT" />
<Button fx:id="exit" layoutX="397.0" layoutY="174.0"
onAction="#handleButtonAction_exit" text="EXIT" />
<TableView fx:id="employeesTableView" layoutX="7.0" layoutY="252.0" minWidth="-
Infinity" nodeOrientation="LEFT_TO_RIGHT" prefHeight="263.0" prefWidth="459.0"
style="-fx-background-color: yellow; -fx-border-color: black;">
<columns>
<TableColumn fx:id="idTableView" minWidth="0.0" prefWidth="61.0" text="Roll no"
/>
<TableColumn fx:id="firstNameTableView" prefWidth="103.0" text="Sem1"
/>
<TableColumn fx:id="lastNameTableView" prefWidth="99.0" text="Sem 2"
/>
<TableColumn fx:id="departmentTableView" prefWidth="93.0" text="Sem 3"
/>
<TableColumn fx:id="lastNameTableView1" prefWidth="99.0" text="Sem 4"
/>
</columns>
<padding>
<Insets bottom="5.0" left="5.0" right="5.0" top="5.0" />
</padding>
</TableView>
<Label layoutX="25.0" layoutY="28.0" text="ROLL NO" />
<Label layoutX="25.0" layoutY="60.0" text="COURSE" />
<RadioButton fx:id="r1" layoutX="108.0" layoutY="60.0"
mnemonicParsing="false" text="MCA" />
<RadioButton fx:id="r2" layoutX="244.0" layoutY="60.0" mnemonicParsing="false"
text="MBA" />
<TextField fx:id="t2" layoutX="127.0" layoutY="101.0" prefHeight="25.0"
prefWidth="69.0" />
<TextField fx:id="t3" layoutX="244.0" layoutY="101.0" prefHeight="25.0"
prefWidth="69.0" />
<TextField fx:id="t4" layoutX="127.0" layoutY="138.0" prefHeight="25.0"
prefWidth="69.0" />
<TextField fx:id="t5" layoutX="244.0" layoutY="142.0" prefHeight="25.0"
prefWidth="69.0" />
<TextField fx:id="t6" layoutX="126.0" layoutY="174.0" prefHeight="25.0"
prefWidth="69.0" />
<TextField fx:id="t1" layoutX="86.0" layoutY="24.0" prefHeight="26.0"
prefWidth="400.0" />
<TextField fx:id="t7" layoutX="244.0" layoutY="174.0" prefHeight="25.0"
prefWidth="69.0" />
<TextField fx:id="t8" layoutX="127.0" layoutY="208.0" prefHeight="25.0"
prefWidth="69.0" />
<TextField fx:id="t9" layoutX="328.0" layoutY="208.0" prefHeight="25.0"
prefWidth="69.0" />
<Label layoutX="53.0" layoutY="105.0" text="YEAR 1" />
<Label layoutX="48.0" layoutY="146.0" text="YEAR 2" />
<Label layoutX="43.0" layoutY="178.0" text="YEAR 3" />
<Label layoutX="39.0" layoutY="212.0" text="TOTAL" />
<Label layoutX="141.0" layoutY="84.0" text="SEM1" />
<Label layoutX="265.0" layoutY="84.0" text="SEM 2" />
<Label layoutX="261.0" layoutY="212.0" text="AVG" />
</children>
</AnchorPane>