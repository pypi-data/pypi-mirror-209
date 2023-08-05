def __check_float(entry_widget):
    try:
        float(entry_widget.get())
        return True
    except:
        return False


def EntryValidation(entry_widget=None, entry_placeholder='', f=0, i=0, i_f=0, s=0, entry_widget_foreground='#272727',
                    placeholder_foreground='#A7A7A7', callMethod=None):
    """
    The EntryValidation function created to  Validate Tkinter Entry widget with customized types like str, int,
    float, float & int values.

    :param entry_widget: Entry widget Instance : Tk Entry Object.
    :param entry_placeholder: Entry Placeholder Text : str.
    :param f: Float Values Accept : Boolean.
    :param i: Integer Values Accept : Boolean.
    :param i_f: Integer & Float Values Accept : Boolean.
    :param s: String Values Accept : Boolean.
    :param entry_widget_foreground: Entry Font Color : str.
    :param placeholder_foreground:  Entry Placeholder Font Color: str.
    :param callMethod: Custom Function will trigger after Focus out of Entry widget.
    :return: Validations
    """
    if entry_widget is not None:
        if entry_placeholder != '':
            entry_widget.insert(0, entry_placeholder)
        if s:
            entry_widget.bind('<FocusIn>', lambda x: entry_widget.delete(0,
                                                                         'end') if entry_widget.get() == entry_placeholder else 'pass')
            entry_widget.bind('<KeyRelease>',
                              lambda x: entry_widget.get() if entry_widget.get().isalpha() else entry_widget.delete(0,
                                                                                                                    'end'))
            entry_widget.bind('<FocusOut>', lambda x: [
                [entry_widget.config(foreground=entry_widget_foreground), [callMethod() if callMethod != None else '']
                 ] if entry_widget.get() != entry_placeholder else 'pass'] if entry_widget.get() != entry_placeholder and len(
                entry_widget.get()) >= 1 else [
                entry_widget.config(foreground=placeholder_foreground), entry_widget.delete(0, 'end'),
                entry_widget.insert(0, entry_placeholder)])
        if f:
            entry_widget.bind('<FocusIn>', lambda x: entry_widget.delete(0,
                                                                         'end') if entry_widget.get() == entry_placeholder else 'pass')
            entry_widget.bind('<KeyRelease>',
                              lambda x: entry_widget.get() if __check_float(entry_widget) else entry_widget.delete(0,
                                                                                                                   'end'))
            entry_widget.bind('<FocusOut>', lambda x: [
                [entry_widget.config(foreground=entry_widget_foreground), [callMethod() if callMethod != None else '']
                 ] if entry_widget.get() != entry_placeholder else 'pass'] if entry_widget.get() != entry_placeholder and len(
                entry_widget.get()) >= 1 else [
                entry_widget.config(foreground=placeholder_foreground), entry_widget.delete(0, 'end'),
                entry_widget.insert(0, entry_placeholder)])
        if i:
            entry_widget.bind('<FocusIn>', lambda x: entry_widget.delete(0,
                                                                         'end') if entry_widget.get() == entry_placeholder else 'pass')
            entry_widget.bind('<KeyRelease>',
                              lambda x: entry_widget.get() if entry_widget.get().isdigit() else entry_widget.delete(0,
                                                                                                                    'end'))
            entry_widget.bind('<FocusOut>', lambda x: [
                [entry_widget.config(foreground=entry_widget_foreground), [callMethod() if callMethod != None else '']
                 ] if entry_widget.get() != entry_placeholder else 'pass'] if entry_widget.get() != entry_placeholder and len(
                entry_widget.get()) >= 1 else [
                entry_widget.config(foreground=placeholder_foreground), entry_widget.delete(0, 'end'),
                entry_widget.insert(0, entry_placeholder)])
        if i_f:
            entry_widget.bind('<FocusIn>', lambda x: entry_widget.delete(0,
                                                                         'end') if entry_widget.get() == entry_placeholder else 'pass')
            entry_widget.bind('<KeyRelease>',
                              lambda x: entry_widget.get() if entry_widget.get().isdigit() or __check_float(
                                  entry_widget) else entry_widget.delete(0, 'end'))
            entry_widget.bind('<FocusOut>', lambda x: [
                [entry_widget.config(foreground=entry_widget_foreground), [callMethod() if callMethod != None else '']
                 ] if entry_widget.get() != entry_placeholder else 'pass'] if entry_widget.get() != entry_placeholder and len(
                entry_widget.get()) >= 1 else [
                entry_widget.config(foreground=placeholder_foreground), entry_widget.delete(0, 'end'),
                entry_widget.insert(0, entry_placeholder)])
    else:
        return 'Warning : Entry Widget is None'
