import {Component, Input, OnInit} from '@angular/core';
import { categories } from './categories';

@Component({
  selector: 'app-applic',
  templateUrl: './applic.component.html',
  styleUrls: ['./applic.component.css']
})
export class ApplicComponent implements OnInit {
  categories = categories;  //
  deletedItemsIds: number[] = []; //
  constructor() {
  }

  ngOnInit(): void {
  }
  categorySelection(id: number): void
  {
    id = id - 1;
    categories[id].visble = !categories[id].visble;
  }
  addBannedId(categoty): void
  {
    categoty.bannedIds = categoty.bannedIds + 1;
  }
}
