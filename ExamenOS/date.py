
#!/user/bin/python

#———————————————————
# ——Date——
#———————————————————
#By Marisol_Martinez_Madrigal


  #include <gtk/gtk.h>

static void fecha (GtkCalendar *calendar,
				gpointer fecha)

{
	unsigned int day;	
	unsigned int month;
	unsigned int year;
	char date [10]

	Gtkwidget *label = lookup_widget (GTK_WIDGET (calendar), “label1”);
	
	gtk_calendar_ get_date(Gtk_CALENDAR(calendar), &day, &month, $year);

	sprintf(fecha, “ % d/ % m/ % y ”, day, month, year);

	gtk_label_set_text(GTK_LABEL(label), (const char *) date);
 
	g_print(“ la fecha actual es \n ”)

 return TRUE;
}