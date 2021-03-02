import { Component, OnInit } from '@angular/core';
import { Input } from '@angular/core';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {
  @Input() productList;
  @Input() visible: boolean;
  deletedItemsIds: number[];
  // here visible: boolean which is = false in constructor and controlls from parent's function directly without input and output
  constructor() {
    this.deletedItemsIds = [];
  }

  ngOnInit(): void {
  }
  deleteId(id: number): void
  {
    this.deletedItemsIds.push(id);
  }

}
