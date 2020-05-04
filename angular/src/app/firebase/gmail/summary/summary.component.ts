import {Component, OnInit} from '@angular/core';

import {AngularFirestore, AngularFirestoreCollection} from '@angular/fire/firestore';
import {Observable} from 'rxjs';

export interface Gmail {
  msg: string;
  date?: string;
}

@Component({
  selector: 'app-summary',
  templateUrl: './summary.component.html',
  styleUrls: ['./summary.component.css']
})
export class SummaryComponent implements OnInit {
  gmails: Observable<any[]>;

  private gmailCollection: AngularFirestoreCollection<Gmail>;

  constructor(private afs: AngularFirestore) {
    this.gmailCollection = afs.collection<Gmail>('gmail/possible/summary');
    this.gmails = this.gmailCollection.valueChanges();

  }

  ngOnInit(): void {
  }

}
