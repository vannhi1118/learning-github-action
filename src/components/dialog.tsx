import { Fragment } from 'react';
import Button from '@mui/material/Button'
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';

export type AlertDialogProps = {
    title?: string,
    message?: string,
    state: boolean,
    handleClose?: () => void
}

export function AlertDialog(props: AlertDialogProps) {

  return (
    <Fragment>
      <Dialog
        open={props.state}
        onClose={props.handleClose}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">
          {props.title}
        </DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            {props.message}
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={props.handleClose} autoFocus id='alert-close-button'>
            OK
          </Button>
        </DialogActions>
      </Dialog>
    </Fragment>
  );
}