import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent implements OnInit {
  @Input() item;
  @Output() idOnRemove = new EventEmitter();
  likes: number;
  constructor() {
    this.likes = 0;
  }
  ngOnInit(): void {
  }
  removeItem(id: number): void
  {
    this.idOnRemove.emit(id);
  }
}
